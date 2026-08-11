# Writing reusable GPU functions with generic pointers

**Framework**: Metal

Define utility functions once for multiple address spaces, and share types with your app’s main code.

#### Overview

Metal Shading Language (MSL) 4.1 and later includes support for generic pointers. Generic pointers in MSL omit the address space annotation and can point to a memory address in the `thread`, `threadgroup`, or `device` address space. In MSL 4.0 and earlier, every pointer in a GPU function requires an explicit address space annotation.

With generic pointers, you write a utility function once, instead of separate, equivalent functions for each combination of address spaces its parameters use. This makes it easier to port code from C++ or other languages that don’t annotate pointers with an address space.

For example, a function that needs one overload per address space in MSL 4.0 collapses to a single generic function in MSL 4.1:

```metal
// In MSL 4.0 and earlier, you need a separate declaration for each address space.
void negate(thread float* value) { *value = -(*value); }
void negate(device float* value) { *value = -(*value); }

// In MSL 4.1 and later, a generic function applies to multiple address space variations.
void negate(float* value) { *value = -(*value); }
```

> **Note**: Generic pointers don’t cover address spaces that require explicit annotations, such as `constant`, `threadgroup_imageblock`, `ray_data`, and `object_data`.

Before adopting generic pointers in your apps, weigh the runtime trade-offs. As you add generic pointers to your MSL types and functions, migrate your existing code by consolidating the MSL 4.0 overloads, and share a single type definition with your app’s regular CPU code.

#### Evaluate the Runtime Trade Offs

The compiler usually identifies each generic pointer’s address space with static analysis and resolves it to a concrete pointer, which adds no runtime cost. In situations where the compiler can’t resolve a generic pointer to a concrete address space, such as across dynamic libraries or for a generic pointer that comes from an argument buffer, the program resolves the address space at runtime and branches to the matching code path. Each branch is relatively fast, but within tight inner loops, the small branching costs can add up and noticeably affect runtime performance. You can avoid the branching runtime costs by providing concrete versions of the function for the relevant call sites, which also compile for MSL 4.0 and earlier.

Generic pointers can also slightly increase register pressure on some GPUs.

#### Write a Generic Function

Because generic pointers omit the address space annotation, a single function can accept pointer arguments from any address space the feature supports. For example, this `accumulate` function has generic pointers as its `total` and `value` parameters:

```metal
/// Adds a floating-point value to a total.
///
/// Compile a generic version of this function by setting the compiler's
/// language to Metal Shading Language (MSL) 4.1 or later.
///
/// - Parameters:
///   - total: A pointer to a floating-point value.
///   - value: A pointer to a constant floating-point value.
void accumulate(float* total, const float* value) {
    *total += *value;
}
```

Compiling this function with MSL 4.1 and later creates a generic implementation that works with any combination of address spaces that generic pointers support. This means that the `accumulate` function’s `total` and `value` arguments can come from any combination of the `thread`, `threadgroup`, and `device` address spaces.

For example, you can pass any of the following arguments to either parameter:

- A `thread` value, such as a local variable
- A `threadgroup` value that multiple threads share
- A `device` value, such as an element within a buffer

> **Note**: In an entry-point function, you need to provide an explicit address space annotation for resource parameters, such as `device` or `threadgroup`.

#### Consolidate Function Overloads

This MSL 4.0 equivalent implementation of the `accumulate` function applies the `thread` address space annotation to both of its pointer parameters:

```metal
/// Adds a floating-point value to a total for thread pointers.
///
/// - Parameters:
///   - total: A pointer to a floating-point value in the `thread` address space.
///   - value: A pointer to a constant floating-point value in the `thread` address space.
void accumulate(thread float* total, const thread float* value) {
    *total += *value;
}
```

In this example, the function only works when both the `total` and `value` arguments point to memory in the `thread` address space. The compiler reports an error at a call site if either argument points to memory in a different address space, such as `device`.

To solve the problem in MSL 4.0, implement a function overload for each unique combination of address space annotations across the call sites:

```metal
/// Adds a floating-point value to a total for device pointers.
///
/// - Parameters:
///   - total: A pointer to a floating-point value in the `device` address space.
///   - value: A pointer to a constant floating-point value in the `device` address space.
void accumulate(device float* total, const device float* value) {
    *total += *value;
}

/// Adds a floating-point value in thread memory to a total in device memory.
///
/// - Parameters:
///   - total: A pointer to a floating-point value in the `device` address space.
///   - value: A pointer to a constant floating-point value in the `thread` address space.
void accumulate(device float* total, const thread float* value) {
    *total += *value;
}
```

The earlier MSL 4.1 version of `accumulate` replaces all of the MSL 4.0 overloads with a single definition with generic pointers.

#### Update Existing Functions

You can convert any of your app’s existing functions to a generic version by removing the address space annotation from one or more of its pointers. For example, the following `maskByte` utility function only works for call sites that pass a pointer to a `threadgroup` memory address:

```metal
void maskByte(threadgroup int* value) {
    *value &= 0xFF;
}
```

The generic equivalent removes the `threadgroup` keyword:

```metal
void maskByte(int* value) {
    *value &= 0xFF;
}
```

A subtler case is a member function that omits an address space annotation. Look for member functions without an address space annotation in code that predates MSL 4.1, and decide whether to let each become generic or give it an explicit `thread` annotation. In MSL 4.0 and earlier, the compiler implicitly qualifies that function’s `this` pointer with `thread`. In MSL 4.1 and later, the same `this` pointer becomes generic.

For example, this `Sphere` type has two member functions:

- `normal_at`, which has no address space annotation for its `this` pointer
- `recenter`, which explicitly annotates its `this` pointer with `thread`

```metal
struct Sphere {
    float3 center;

    float3 normal_at(float3 point) const {
        return normalize(point - center);
    }

    void recenter(float3 origin) thread {
        center = origin;
    }
};
```

Recompiling this type with MSL 4.1 requires no source changes. The `recenter` function stays `thread` because of its explicit annotation, but the `normal_at` function becomes generic.

> **Note**: A member function’s implicit `this` is the only pointer that compiles without an address space annotation in MSL 4.0, and it’s the only pointer that implicitly becomes generic in MSL 4.1.

You can preserve the behavior of your existing MSL 4.0 member functions before migrating them to MSL 4.1 or later, by compiling with the `-Wmetal-addr-spaces` option and applying the compiler’s fix-its:

```shell

% xcrun metal -std=metal4.0 -Wmetal-addr-spaces -Xclang -fixit -fsyntax-only Kernels.metal

```

The command includes the following options that modify the Metal compiler’s default behavior:

- **`-std=metal4.0`**: Sets the Metal Shading Language version to `4.0`.
- **`-Wmetal-addr-spaces`**: Generates a Metal-specific warning when the compiler detects member functions that don’t have an address space annotation.
- **`-Xclang -fixit`**: Applies fix-it hints from the diagnostics by rewriting those parts of the source code file in place. The `-Xclang` portion tells the command to pass the `-fixit` option directly to the compiler’s front end.
- **`-fsyntax-only`**: Limits the compilation to the semantic analysis phase, before code generation or linking. With this option, the command exits with a success value (`0`) because it stops the compiler before the linking phase, which would fail anyway because the `-fixit` prevents the compiler from producing any linkable outputs.

The fix-it option rewrites the source in place by adding an explicit `thread` annotation to each unannotated member function, including constructors:

```metal
struct Sphere {
    float3 center;

    float3 normal_at(float3 point) const thread {
        return normalize(point - center);
    }

    void recenter(float3 origin) thread {
        center = origin;
    }
};
```

> 💡 **Tip**: Consider preserving a copy of the original code before running the command with `-Xclang -fixit`.

#### Share Types Between Host and Device

Generic pointers also apply to a pointer member inside a structure. A type that holds a pointer can have the same definition on the host and the device, so your app and its GPU functions can share a single header.

Consider a C++ structure in a header file that both C++ and MSL source files can share. The `LightData` structure has a `lights` pointer to an array of `Light` instances:

```cpp
// For the app's C++ code, `float3` comes from the SIMD library's `simd::float3` type.
#ifndef __METAL_VERSION__
#include <simd/simd.h>
using float3 = simd::float3;
#endif

struct Light {
    float3 position;
    float3 direction;
    float3 color;
    float intensity;
};

struct LightData {
    Light* lights;
    unsigned light_count;
};
```

In MSL 4.1, `LightData` compiles without any changes, because its `lights` member becomes a generic pointer:

```metal
// A C++ structure that compiles in MSL 4.1 without changes.
struct LightData {
    Light* lights;          // A generic pointer in MSL 4.1.
    unsigned light_count;
};

fragment float4 shade_fragment(device LightData& lighting) {
    // ...
}
```

In MSL 4.0, the `lights` member needs an explicit address space annotation. In this example, the `device` annotation in the MSL declaration diverges from the app’s original declaration:

```metal
// A C++ structure requires a change for MSL 4.0 and earlier.
struct LightData {
    device Light* lights;   // A pointer in MSL 4.0 requires an address space annotation.
    unsigned light_count;
};
```

With MSL, both source files can share one definition for a type in a common header, which is easier to maintain than separate, language-specific copies of common types.

#### Define Member Functions Once

A single generic definition in MSL 4.1 and later can replace a set of overloads. The following `RowMatrix` type defines its member functions and operators once, which the project can share with its C++ code and its MSL 4.1 code:

```metal
// For the app's C++ code, `float3`, `dot`, and `normalize` come from the SIMD library.
#ifndef __METAL_VERSION__
#include <simd/simd.h>
using float3 = simd::float3;
using simd::dot;
using simd::normalize;
#endif

// Common types for C++ and MSL 4.1 code.
struct RowMatrix {
    float3 row0, row1, row2;

    RowMatrix& orthonormalize() {
        row0 = normalize(row0);
        row1 -= dot(row0, row1) * row0;
        row1 = normalize(row1);
        row2 -= dot(row0, row2) * row0 + dot(row1, row2) * row1;
        row2 = normalize(row2);
        return *this;
    }

    RowMatrix& operator*=(const RowMatrix& other) {
        row0 *= other.row0;
        row1 *= other.row1;
        row2 *= other.row2;
        return *this;
    }
};
```

These member functions omit all address space annotations, so they can serve any combination of pointers from the address spaces the feature supports:

- `device`
- `thread`
- `threadgroup`

A kernel can call those member functions with any combination of pointers in different address spaces:

```metal
kernel void combine_matrices(device RowMatrix& result,
                             const device RowMatrix& factor) {
    RowMatrix scratch = { float3(1), float3(2), float3(3) };
    result *= scratch.orthonormalize();
    result *= factor;
    result.orthonormalize();
}
```

In this example, the `result` and `factor` parameters point to `device` memory, and `scratch` is a `thread`-local value. When a GPU function calls a member function on `scratch`, its implicit `this` points to `thread` memory. The generic definitions of the member functions support all of these pointer combinations.

#### Consolidate Member Function Overloads

To implement the same support with function overloads, which MSL 4.0 and earlier requires, provide an implementation for each unique combination of parameter pointers across all of the call sites.

A member function signature lists address space annotations in three places:

- The return value
- Each pointer parameter
- The annotation for the type’s implicit `this` parameter, which is at the end of a member function’s signature

You only need to define an overload for each unique combination of the pointer *parameters*, not for the return value. The return value doesn’t contribute to a member function’s signature.

> **Note**: In C++ and MSL, defining two functions that only differ by return type is an error, because the return type isn’t part of the signature. This is different from Swift, which allows overloads that only differ by return type.

In the following example, the `orthonormalize()` member function has only one parameter, the implicit `this`:

```metal
device RowMatrix& orthonormalize() device
```

This means that the member function only needs an overload for each unique address space for the `this` pointer. For example, when every call site for `orthonormalize()` is from a `RowMatrix` instance in either `thread` or `device` memory, the code only needs to define two overloads, one for each address space possibility for the `this` parameter:

```metal
// Define the `device` and `thread` address space overloads for `orthonormalize()`.
device RowMatrix& orthonormalize() device { /* ... */ }
thread RowMatrix& orthonormalize() thread { /* ... */ }
```

> **Note**: The address space annotation of a member function’s return value typically follows the `this` pointer’s annotation.

The number of potential overloads multiplies with each additional parameter. For example, the `*=` operator has two parameters: `other`, and the implicit `this` pointer.

```metal
device RowMatrix& operator*=(const device RowMatrix& other) device
```

In this case, the declaration annotates both parameters with the `device` keyword. Covering all possible combinations of the `device` and `thread` address spaces requires four overloads, as shown here:

```metal
// Define the `device` and `thread` address space overloads for the `*=` operator.
device RowMatrix& operator*=(const device RowMatrix& other) device { /* ... */ }
device RowMatrix& operator*=(const thread RowMatrix& other) device { /* ... */ }
thread RowMatrix& operator*=(const thread RowMatrix& other) thread { /* ... */ }
thread RowMatrix& operator*=(const device RowMatrix& other) thread { /* ... */ }
```

Satisfying all combinations of the arguments and their applicable address spaces can require many overloads. In this example, adding support for the `threadgroup` address space brings the total to 12 overloads: three for the `orthonormalize()` function, and nine for the `*=` operator:

```metal
// The `device`, `thread`, and `threadgroup` overloads for `orthonormalize()`.
device RowMatrix& orthonormalize() device { /* ... */ }
thread RowMatrix& orthonormalize() thread { /* ... */ }
threadgroup RowMatrix& orthonormalize() threadgroup { /* ... */ }

// The `device`, `thread`, and `threadgroup` overloads for `*=`
// when `this` is in `device` memory.
device RowMatrix& operator*=(const device RowMatrix& other) device { /* ... */ }
device RowMatrix& operator*=(const thread RowMatrix& other) device { /* ... */ }
device RowMatrix& operator*=(const threadgroup RowMatrix& other) device { /* ... */ }

// Define the `device`, `thread`, and `threadgroup` overloads for `*=`
// when `this` is in `thread` memory.
thread RowMatrix& operator*=(const device RowMatrix& other) thread { /* ... */ }
thread RowMatrix& operator*=(const thread RowMatrix& other) thread { /* ... */ }
thread RowMatrix& operator*=(const threadgroup RowMatrix& other) thread { /* ... */ }

// Define the `device`, `thread`, and `threadgroup` overloads for `*=`
// when `this` is in `threadgroup` memory.
threadgroup RowMatrix& operator*=(const device RowMatrix& other) threadgroup { /* ... */ }
threadgroup RowMatrix& operator*=(const thread RowMatrix& other) threadgroup { /* ... */ }
threadgroup RowMatrix& operator*=(const threadgroup RowMatrix& other) threadgroup { /* ... */ }
```

However, a single, generic member function in MSL 4.1 and later replaces all of the overloads your app needs for each member function in MSL 4.0 and earlier. For example, the original operator implementation of the `RowMatrix` structure in the C++ header file is the MSL generic equivalent that eliminates the need to implement separate overloads:

```metal
RowMatrix& operator*=(const RowMatrix& other) {
    row0 *= other.row0;
    row1 *= other.row1;
    row2 *= other.row2;
    return *this;
}
```

#### Cast Between Address Spaces

A generic function works across address spaces, but sometimes one path inside it needs a concrete pointer, such as a 64-bit atomic operation that only runs on a `device` pointer. Casting keeps a function generic while it converts a pointer to a concrete address space where a path needs it.

The compiler implicitly converts a concrete pointer to a generic one without an operator:

```metal
thread int value = 42;

// Convert a thread pointer to a generic pointer implicitly.
int* generic = &value;
```

MSL has two operators that cast a generic pointer to a concrete address space:

- `static_cast`
- `addrspace_cast`

The `static_cast` operator converts a generic pointer to a concrete pointer without a runtime check. Apply the static cast when you know which address space the generic pointer points to.

```metal
// Valid, because `generic` refers to thread memory.
thread int* concrete = static_cast<thread int*>(generic);
```

The conversion is only valid when the generic pointer refers to the address space in the cast operator. Invalid conversions can lead to incorrect behavior or results. When you enable Shader Validation, it detects these invalid conversions during development. For more information, see [`Validating your app’s Metal shader usage`](https://developer.apple.com/documentation/Xcode/Validating-your-apps-Metal-shader-usage).

> **Note**: Casting a null pointer returns a null pointer.

The `addrspace_cast` operator also converts a generic pointer to a concrete one but adds a runtime check:

```metal
// `generic` refers to thread memory, so this cast returns `nullptr`.
device int* maybe_device = addrspace_cast<device int*>(generic);

if (maybe_device != nullptr) {
    // The `generic` pointer refers to an address in device memory.
}
```

The cast returns a valid concrete pointer when the generic pointer refers to that address space; otherwise `nullptr`. The `addrspace_cast` operator is a safe choice when your code doesn’t know a generic pointer’s address space in advance.

You can test a generic pointer’s address space without casting it by calling one of the built-in MSL functions:

- `is_thread_addrspace()`
- `is_device_addrspace()`
- `is_threadgroup_addrspace()`

Each function returns a Boolean value that indicates whether a generic pointer refers to that address space:

```metal
if (is_thread_addrspace(generic)) {
    // Safe, because the check confirms the thread address space.
    thread int* concrete = static_cast<thread int*>(generic);
}
```

Each test is equivalent to casting the generic pointer with `addrspace_cast` and checking that the result isn’t equal to `nullptr`.

> **Note**: The testing functions return `false` for arguments that equal `nullptr`.

#### Prevent Abi Mismatches

MSL 4.1 alters how the compiler applies name decoration to function names, which creates an application binary interface (ABI) boundary at the language-version level. This boundary applies to any GPU binaries you link together, whether you distribute them in a binary archive, a dynamic library, or a Metal library. For example, linking a component you compile with MSL 4.0 and another you compile with MSL 4.1 can result in incorrect runtime behavior, even when both components contain only intermediate representation (IR) code.

> ❗ **Important**: The Metal compiler and the linker don’t detect binary mismatches between MSL versions.

To avoid this scenario, compile everything you link together with the same MSL language version. This works because it’s the version of the MSL *language* that affects the ABI, not the compiler’s version. You can compile source and IR files for MSL 4.0 with a newer compiler that also supports MSL 4.1 or later, and the output binaries link correctly with other MSL 4.0 binaries.

## See Also

- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)
  Control when and how you compile an app’s shaders.
- [Shader libraries](shader-libraries.md)
  Manage and load your app’s Metal shaders.
- [Using function specialization to build pipeline variants](using-function-specialization-to-build-pipeline-variants.md)
  Create pipelines for different levels of detail from a common shader source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/writing-reusable-gpu-functions-with-generic-pointers)*