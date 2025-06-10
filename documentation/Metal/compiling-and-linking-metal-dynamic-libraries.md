# Compiling and Linking Metal Dynamic Libraries

**Framework**: Metal

Build a Metal dynamic library from the command line, allowing for runtime loading of shared shaders.

#### Overview

When you share a set of utility functions between multiple Metal libraries, static linking at compile time includes those functions in all of your libraries. This causes libraries to increase in size because each Metal library includes duplicate code for the utility functions. Metal also compiles individual, identical versions of your utilites for each library, causing longer shader compilation times.

Metal offers dynamic libraries with runtime loading to solve these problems — you compile your utilities into a dynamic library and link other Metal libraries to it, giving a single source for your utility functions.

This article tells you how to build a dynamic library from the command line with the Metal compiler, add binary archives, and then link your dynamic library to another Metal library. Your app then loads your linked library at runtime. This article uses the following filenames in code examples:

- `utilities.metal`, a metal source file that contains your utility functions
- `shaders.ir`, an intermediate representation from the Metal compiler containing shaders that call functions in `utilities.metal`

For instructions on compiling an intermediate representation for Metal, see [`Building a Shader Library by Precompiling Source Files`](building-a-shader-library-by-precompiling-source-files.md). For an example of an app that builds and links dynamic libraries at runtime, see [`Creating a Metal Dynamic Library`](creating-a-metal-dynamic-library.md).

##### Compile Shaders to a Dynamic Library

Start by compiling your utility functions to a dynamic library. Use the `metal` command-line tool, adding both the `-dynamiclib` and `-install_name` options. The `-dynamiclib` flag builds the output as a dynamic library, and `-install_name` is the library name that the linker uses to resolve the library. The following compiler invocation builds `utilities.metal` to a dynamic library `libUtility.ir.metallib`, where you link the library as `Utility`:

```shell
% xcrun -sdk macosx metal -dynamiclib utilities.metal -o libUtility.ir.metallib -install_name libUtility.metallib
```

> ❗ **Important**:  Ensure that the install name uses the format of l`ib${LIBRARY_NAME}.metallib`. Otherwise, the Metal linker can’t locate your dynamic library.

##### Add Binary Archives to Your Dynamic Library Optionally

Binary archives are prebuilt shader functions for GPUs you specify at compile time. Use binary archives when you prefer to make the tradeoff of distributing larger files for your app while avoiding the cost of compiling shaders from Metal IR at runtime. For more information on binary archives, see [`Metal Binary Archives`](metal-binary-archives.md).

The Metal translator allows you to create a dynamic library with GPU-specific binaries alongside the Metal IR slices. The code example below provides the command-line arguments that `metal-tt` uses to add Metal 3 binaries to `libUtility.metalir.metallib`. Then, the combined output writes to `libUtility.metallib`.

```shell
% xcrun -sdk macosx metal-tt libUtility.metalir.metallib -o libUtility.metallib $(xcrun -sdk macosx metal-config --native-arch-flags --gpu-family=metal3)
```

For more information on `metal-config`, run `man metal-config` in Terminal.

For more information about the Metal translator and how you can customize which binaries to build from a Metal IR file, see [`Creating Binary Archives from Device-Built Pipeline State Objects`](creating-binary-archives-from-device-built-pipeline-state-objects.md) and [`Compiling Binary Archives from a Custom Configuration Script`](compiling-binary-archives-from-a-custom-configuration-script.md).

##### Link Utility Shaders to Your Metal Library

Prelinking dynamic libraries to your other libraries avoids some runtime costs associated with resolving the symbols to load from your dynamic library. When you’re compiling your final Metal libraries to ship, use the `-L` and `-l` linker options with the `metal` command-line tool. The `-l` option provides the names of libraries to link to, and `-L` provides custom library search paths. The following code example demonstrates linking an intermediate representation `shaders.ir` with the `Utilities` library that you compile from the previous step. If you skip compiling binaries into your dynamic library, rename `libUtility.metalir.metallib` to `libUtility.metallib`.

```shell
% # Uncomment the next line to rename the library if you need to.
% # mv libUtility.metalir.metallib libUtility.metallib
% xcrun -sdk macosx metal shaders.ir -o shaders.metallib -lUtility -L ./
```

Add both `shaders.metallib` and `libUtility.metallib` to your Xcode project as resources. For your dynamic library to load correctly if you link it from the command line, place it at a location in your app’s resources corresponding to the path that you set for the `-L` argument. In this example, put `shaders.metallib` and l`ibUtility.metallib` in the same directory in a resource bundle.

##### Load Dynamic Libraries in Your App

Use the [`makeDynamicLibrary(url:)`](mtldevice/makedynamiclibrary(url:).md) method in your app to load your Metal dynamic library, and then add it to a pipeline descriptor calling the shader functions in your other Metal libraries. The following code example loads a dynamic library and creates an [`MTLComputePipelineDescriptor`](mtlcomputepipelinedescriptor.md) that includes it as a library to load:

## See Also

- [Creating a Metal Dynamic Library](creating-a-metal-dynamic-library.md)
  Compile a library of shaders and write it to a file as a dynamically linked library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/compiling-and-linking-metal-dynamic-libraries)*