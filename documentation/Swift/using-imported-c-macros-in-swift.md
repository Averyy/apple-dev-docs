# Using Imported C Macros in Swift

**Framework**: Swift

Use imported C-defined macros as constants.

#### Overview

Swift automatically imports simple, constant-like macros, declared with the `#define` directive, as global constants. Macros are imported when they use literals for string, floating-point, or integer values, or use operators like `+`, `-`, `>`, and `==` between literals or previously defined macros. This example defines some simple macros in a C header:

```occ
#define FADE_ANIMATION_DURATION 0.35
#define VERSION_STRING "2.2.10.0a"
#define MAX_RESOLUTION 1268

#define HALF_RESOLUTION (MAX_RESOLUTION / 2)
#define IS_HIGH_RES (MAX_RESOLUTION > 1024)
```

When imported into Swift, the macros in the above example are equivalent to these constant declarations:

```swift
let FADE_ANIMATION_DURATION = 0.35
let VERSION_STRING = "2.2.10.0a"
let MAX_RESOLUTION = 1268

let HALF_RESOLUTION = 634
let IS_HIGH_RES = true
```

##### Use Functions and Generics Instead of Complex Macros

C macros that are more complex than simple constant definitions have no counterpart in Swift. You use complex macros in C and Objective-C to avoid type-checking constraints or to avoid retyping large amounts of boilerplate code. However, macros can make debugging and refactoring difficult. In Swift, you can use functions and generics to achieve the same results without any compromises.

## See Also

- [Using Imported C Structs and Unions in Swift](using-imported-c-structs-and-unions-in-swift.md)
  Learn how Swift represents imported C structures and unions, including types with bitfields and unnamed fields.
- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)
  Learn how to call imported functions that are declared in a C header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/using-imported-c-macros-in-swift)*