# Marking API Availability in Objective-C

**Framework**: Swift

Use `a` macro to denote the availability of an Objective-C API.

#### Overview

In Swift, you use the `@available` attribute to control whether a declaration is available to use when building an app for a particular target platform. Similarly, you use the availability condition `#available` to execute code conditionally based on required platform and version conditions. Both kinds of availability specifier are also available in Objective-C.

For detailed information about specifying platform availability, see [`Declaration Attributes`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Attributes.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

##### Mark Availability

Use the `API_AVAILABLE` macro to add availability information in Objective-C:

```occ
@interface MyViewController : UIViewController
- (void) newMethod API_AVAILABLE(ios(11), macosx(10.13));
@end
```

This is equivalent to using the `@available` attribute on a declaration in Swift:

```swift
@available(iOS 11, macOS 10.13, *)
func newMethod() {
    // Use iOS 11 APIs.
}
```

##### Check Availability

Use the `@available()` keyword to check availability information in a conditional statement in Objective-C:

```occ
if (@available(iOS 11, *)) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

This is equivalent to the following conditional in Swift:

```swift
if #available(iOS 11, *) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

## See Also

- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md)
  Use nullability annotations or mark regions as annotated to control how Objective-C declarations are imported into Swift.
- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md)
  Use the `NS_SWIFT_NAME` macro to customize API names for Swift.
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md)
  Use the `NS_REFINED_FOR_SWIFT` macro to change how an API is imported into Swift.
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md)
  Add macros to your Objective-C types to group their values in Swift.
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md)
  Use the `NS_SWIFT_UNAVAILABLE` macro to prevent an API from being used in Swift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/marking-api-availability-in-objective-c)*