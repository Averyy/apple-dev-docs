# Objective-C and C Code Customization

**Framework**: Swift

Apply macros to your Objective-C APIs to customize how they’re imported into Swift.

## Topics

### Customizing Objective-C APIs
- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md)
  Use nullability annotations or mark regions as annotated to control how Objective-C declarations are imported into Swift.
- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md)
  Use the `NS_SWIFT_NAME` macro to customize API names for Swift.
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md)
  Use the `NS_REFINED_FOR_SWIFT` macro to change how an API is imported into Swift.
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md)
  Add macros to your Objective-C types to group their values in Swift.
- [Marking API Availability in Objective-C](marking-api-availability-in-objective-c.md)
  Use a macro to denote the availability of an Objective-C API.
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md)
  Use the `NS_SWIFT_UNAVAILABLE` macro to prevent an API from being used in Swift.
### Customizing C APIs
- [Customizing Your C Code for Swift](customizing-your-c-code-for-swift.md)
  Use the `CF_SWIFT_NAME` macro to group functions that have related behavior.

## See Also

- [Migrating Your Objective-C Code to Swift](migrating-your-objective-c-code-to-swift.md)
  Learn the recommended steps to migrate your code.
- [Cocoa Design Patterns](cocoa-design-patterns.md)
  Adopt and interoperate with Cocoa design patterns in your Swift apps.
- [Handling Dynamically Typed Methods and Objects in Swift](handling-dynamically-typed-methods-and-objects-in-swift.md)
  Cast instances of the Objective-C `id` type to a specific Swift type.
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md)
  Use selectors and key paths to interact with dynamic Objective-C APIs.
- [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)
  Use native Swift syntax to interoperate with types and functions in C and Objective-C.
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md)
  Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/objective-c-and-c-code-customization)*