# Renaming Objective-C APIs for Swift

**Framework**: Swift

Use the `NS_SWIFT_NAME` macro to customize API names for Swift.

#### Overview

If you want to import an Objective-C API into Swift with a different name, use the `NS_SWIFT_NAME` macro. The macro preserves the Objective-C name for use with Objective-C code, so the API has appropriate names in each language.

You apply the `NS_SWIFT_NAME` macro to an individual type, method, or function declaration in Objective-C. After applying the macro, the name you use in your Swift code will be what you’ve chosen by using the macro.

##### Rename Apis

The example below renames a class and one of its properties:

```occ
NS_SWIFT_NAME(Sandwich.Preferences)
@interface SandwichPreferences : NSObject

@property BOOL includesCrust NS_SWIFT_NAME(isCrusty);

@end

@interface Sandwich : NSObject
@end
```

The `SandwichPreferences` class and its `includesCrust` property are renamed to `Sandwich.Preferences` and `isCrusty` for Swift:

```swift
var preferences = Sandwich.Preferences()
preferences.isCrusty = true
```

You use the `NS_SWIFT_NAME` macro as a prefix for classes and protocols. For all other kinds of declaration—such as properties, enumeration cases, and type aliases—you use the macro as a suffix. The following example uses the macro as a suffix to rename an enumeration:

```occ
typedef NS_ENUM(NSInteger, SandwichBreadType) {
    brioche, pumpernickel, pretzel, focaccia
} NS_SWIFT_NAME(SandwichPreferences.BreadType);
```

## See Also

- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md)
  Use nullability annotations or mark regions as annotated to control how Objective-C declarations are imported into Swift.
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md)
  Use the `NS_REFINED_FOR_SWIFT` macro to change how an API is imported into Swift.
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md)
  Add macros to your Objective-C types to group their values in Swift.
- [Marking API Availability in Objective-C](marking-api-availability-in-objective-c.md)
  Use a macro to denote the availability of an Objective-C API.
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md)
  Use the `NS_SWIFT_UNAVAILABLE` macro to prevent an API from being used in Swift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/renaming-objective-c-apis-for-swift)*