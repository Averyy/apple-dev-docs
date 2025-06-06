# Handling Dynamically Typed Methods and Objects in Swift

**Framework**: Swift

Cast instances of the Objective-C `id` type to a specific Swift type.

#### Overview

In Objective-C, the `id` type represents objects that are instances of any Objective-C class. The `id` type is instead imported by Swift as the `Any` type. When you pass a Swift instance to an Objective-C API, it’s bridged as an `id` parameter so that it’s usable in the API as an Objective-C object. When `id` values are imported into Swift as `Any`, the runtime automatically handles bridging back to either class references or value types.

```swift
var x: Any = "hello" as String
x as? String   // String with value "hello"
x as? NSString // NSString with value "hello"

x = "goodbye" as NSString
x as? String   // String with value "goodbye"
x as? NSString // NSString with value "goodbye"
```

##### Downcast Objects to Call Methods and Access Properties

When you work with objects of type `Any` where you know the underlying type, it’s often useful to downcast those objects to the underlying type. However, because the `Any` type can refer to any type, a downcast to a more specific type isn’t guaranteed by the compiler to succeed.

You can use the conditional type cast operator (`as?`), which returns an optional value of the type you are trying to downcast to:

```swift
let userDefaults = UserDefaults.standard
let lastRefreshDate = userDefaults.object(forKey: "LastRefreshDate") // lastRefreshDate is of type Any?
if let date = lastRefreshDate as? Date {
    print("\(date.timeIntervalSinceReferenceDate)")
}
```

If you’re completely certain about the type of the object, you can use the forced downcast operator (`as!`) instead.

```swift
let myDate = lastRefreshDate as! Date
let timeInterval = myDate.timeIntervalSinceReferenceDate
```

However, if a forced downcast fails, a runtime error is triggered:

```swift
let myDate = lastRefreshDate as! String // Error
```

## See Also

- [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)
  Apply macros to your Objective-C APIs to customize how they’re imported into Swift.
- [Migrating Your Objective-C Code to Swift](migrating-your-objective-c-code-to-swift.md)
  Learn the recommended steps to migrate your code.
- [Cocoa Design Patterns](cocoa-design-patterns.md)
  Adopt and interoperate with Cocoa design patterns in your Swift apps.
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md)
  Use selectors and key paths to interact with dynamic Objective-C APIs.
- [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)
  Use native Swift syntax to interoperate with types and functions in C and Objective-C.
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md)
  Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift)*