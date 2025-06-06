# Imported C and Objective-C APIs

**Framework**: Swift

Use native Swift syntax to interoperate with types and functions in C and Objective-C.

#### Overview

You can access and use pieces of code written in C and Objective-C from within your Swift code. After you import an Objective-C framework, a C library, or a header file, you can work with Objective-C classes and protocols, as well as common C constructs, functions, and patterns.

## Topics

### Swift and Objective-C in the Same Project
- [Importing Objective-C into Swift](importing-objective-c-into-swift.md)
  Access classes and other declarations from your Objective-C code in Swift.
- [Importing Swift into Objective-C](importing-swift-into-objective-c.md)
  Access Swift types and declarations from within your Objective-C codebase.
### Cocoa Frameworks
- [Working with Foundation Types](working-with-foundation-types.md)
  Use bridged Foundation types in your Swift codebase to work with dates, times, and other values.
- [Working with Core Foundation Types](working-with-core-foundation-types.md)
  Work directly with memory-managed Core Foundation types in your Swift code, and manually handle retains as needed.
### Objective-C APIs
- [Using Imported Lightweight Generics in Swift](using-imported-lightweight-generics-in-swift.md)
  Understand the constraints of imported Obj-C lightweight generic type declarations.
- [Using Imported Protocol-Qualified Classes in Swift](using-imported-protocol-qualified-classes-in-swift.md)
  Learn how imported Objective-C protocol-qualified classes and metaclasses are represented.
### C APIs
- [Using Imported C Structs and Unions in Swift](using-imported-c-structs-and-unions-in-swift.md)
  Learn how Swift represents imported C structures and unions, including types with bitfields and unnamed fields.
- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)
  Learn how to call imported functions that are declared in a C header.
- [Using Imported C Macros in Swift](using-imported-c-macros-in-swift.md)
  Use imported C-defined macros as constants.

## See Also

- [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)
  Apply macros to your Objective-C APIs to customize how they’re imported into Swift.
- [Migrating Your Objective-C Code to Swift](migrating-your-objective-c-code-to-swift.md)
  Learn the recommended steps to migrate your code.
- [Cocoa Design Patterns](cocoa-design-patterns.md)
  Adopt and interoperate with Cocoa design patterns in your Swift apps.
- [Handling Dynamically Typed Methods and Objects in Swift](handling-dynamically-typed-methods-and-objects-in-swift.md)
  Cast instances of the Objective-C `id` type to a specific Swift type.
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md)
  Use selectors and key paths to interact with dynamic Objective-C APIs.
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md)
  Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/imported-c-and-objective-c-apis)*