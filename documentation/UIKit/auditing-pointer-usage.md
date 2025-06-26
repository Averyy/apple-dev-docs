# Auditing pointer usage

**Framework**: UIKit

Ensure that the pointers in your code are safe for the 64-bit runtime.

#### Overview

Pointers reference objects and other data in memory and are used often in C and Objective-C for passing objects to functions or manipulating the contents of memory. When you update from 32-bit to 64-bit architecture, the pointers in your code double in size, with implications throughout the code. Any assumptions that you make about pointer sizes can lead to undefined behavior, memory corruption, or crashes.

To review your code for proper pointer usage, look for areas where a pointer is being cast, or coerced, to another type. Avoid casting pointers to other types, such as integers. If you print the values of pointers using functions such as `NSLog` or `printf,` use properly prescribed macros in your format string to ensure that values are displayed correctly.

##### Cast Pointers to Integers Selectively

When you cast pointers to an integer type, use pointer types consistently to ensure that all of your variables are large enough to hold an address.

The code below casts a pointer to an `int` type to perform arithmetic on the address. In the 32-bit runtime, this code works because an `int` type and a pointer are the same size. However, in the 64-bit runtime, a pointer is larger than an `int` type, so the assignment loses some of the pointer’s data. To address this, remove the casts. The compiler-generated code now advances the pointer correctly.

```objc
int *c = something passed in as an argument....

int *d = (int *)((int)c + 4); // Incorrect.

int *d = c + 1;               // Correct.
```

If you must cast a pointer to an integer type, always use the `uintptr_t` type to avoid truncation. Note that modifying pointer values through integer math and then converting them back into a pointer can violate basic type aliasing rules. This can lead to unexpected behavior from the compiler as well as processor faults when a misaligned pointer is accessed.

##### Allocate Memory Using Sizeof

Always use `sizeof` to obtain the correct size for any structure or variable you allocate. Never call `malloc` with an explicit size to allocate space for a variable.

```objc
// Incorrect.
uint32_t *x = (uint32_t *)malloc(4);

// Correct.
uint32_t *x = (uint32_t *)malloc(sizeof(uint32_t));
```

Search your code for any instance of `malloc` that isn’t followed by `sizeof`.

##### Access Objective C Internal Structures Using Approved Methods

If you have code that directly accesses an object’s `isa` field, that code fails when executing in the 64-bit runtime, because the `isa` field no longer holds a pointer. Instead, it includes some pointer data and uses the remaining bits to hold other runtime information.

To read an object’s `isa` field, use the class property or call the doc://com.apple.documentation/documentation/objectivec/1418629-object_getclass function instead. To write to an object’s `isa` field, call the doc://com.apple.documentation/documentation/objectivec/1418905-object_setclass function.

> ❗ **Important**:  The Simulator app doesn’t detect the errors described here. Always test your app on actual hardware.

##### Update Format Strings

Print functions, such as `printf`, can be difficult to write when your code has to support both the 32-bit and 64-bit runtimes, because the data types change from one runtime to the other. To solve this problem for standard types and pointer-sized integers, use the various macros listed in the following tables.

| Standard types | Format string |
| --- | --- |
| `int` | `%d` |
| `long` | %ld |
| `long long` | %lld |
| `size_t` | %zu |
| `ptrdiff_t` | %td |
| any pointer | %p |

| Pointer-sized integer type | Format string |
| --- | --- |
| `int[N]_t` (such as `int32_t`) | `PRId[N]` (such as `PRId32`) |
| `uint[N]_t` | `PRIu[N]` |
| `int_least[N]_t` | `PRIdLEAST[N]` |
| `uint_least[N]_t` | `PRIuLEAST[N]` |
| `int_fast[N]_t` | `PRIdFAST[N]` |
| `uint_fast[N]_t` | `PRIuFAST[N]` |
| `intptr_t` | `PRIdPTR` |
| `uintptr_t` | `PRIuPTR` |
| `intmax_t` | `PRIdMAX` |
| `uintmax_t` | `PRIuMAX` |

This example code prints an `intptr_t` variable (a pointer-sized integer) and a pointer.

```objc
#include <inttypes.h>
void *foo;
intptr_t k = (intptr_t) foo;
void *ptr = &k;

printf("The value of k is %" PRIdPTR "\n", k);
printf("The value of ptr is %p\n", ptr);
```

## See Also

- [Updating data structures](updating-data-structures.md)
  Review your app’s data design and update it to conform with 64-bit architecture.
- [Managing functions and function pointers](managing-functions-and-function-pointers.md)
  Ensure that your code correctly handles functions, function pointers, and Objective-C messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/auditing-pointer-usage)*