# SafariSettings.CookiePolicy

**Framework**: ManagedSettings  
**Kind**: enum

The conditions under which Safari accepts cookies.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum CookiePolicy
```

## Topics

### Accepting Cookies
- [SafariSettings.CookiePolicy.always](safarisettings/cookiepolicy-swift.enum/always.md)
  A policy that indicates the device accepts cookies from all websites.
- [SafariSettings.CookiePolicy.currentWebsite](safarisettings/cookiepolicy-swift.enum/currentwebsite.md)
  A policy that indicates the device only accepts cookies from the current website.
- [SafariSettings.CookiePolicy.never](safarisettings/cookiepolicy-swift.enum/never.md)
  A policy that indicates the device doesn’t accept cookies from any website.
- [SafariSettings.CookiePolicy.visitedWebsites](safarisettings/cookiepolicy-swift.enum/visitedwebsites.md)
  A policy that indicates the device only accepts cookies from websites in the user’s browsing history.
### Getting the Range
- [static func != (Self, Self) -> Bool](safarisettings/cookiepolicy-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func ... (Self) -> PartialRangeThrough<Self>](safarisettings/cookiepolicy-swift.enum/'...(_:)-1u7oy.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](safarisettings/cookiepolicy-swift.enum/'...(_:)-7kfn5.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](safarisettings/cookiepolicy-swift.enum/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [var hashValue: Int](safarisettings/cookiepolicy-swift.enum/hashvalue.md)
- [func hash(into: inout Hasher)](safarisettings/cookiepolicy-swift.enum/hash(into:).md)
### Operators
- [static func < (SafariSettings.CookiePolicy, SafariSettings.CookiePolicy) -> Bool](safarisettings/cookiepolicy-swift.enum/_(_:_:).md)
  Returns a Boolean value that indicates whether the value of the first argument is less than that of the second argument.
### Initializers
- [init?(rawValue: String)](safarisettings/cookiepolicy-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var description: String](safarisettings/cookiepolicy-swift.enum/description.md)
  A textual representation of this instance.
- [var rawValue: String](safarisettings/cookiepolicy-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [SafariSettings.CookiePolicy.RawValue](safarisettings/cookiepolicy-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Comparable Implementations](safarisettings/cookiepolicy-swift.enum/comparable-implementations.md)
- [Equatable Implementations](safarisettings/cookiepolicy-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](safarisettings/cookiepolicy-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var cookiePolicy: SafariSettings.CookiePolicy?](safarisettings/cookiepolicy-swift.property.md)
  Defines the conditions under which Safari accepts cookies.
- [static let cookiePolicy: SettingMetadata<SafariSettings.CookiePolicy>](safarisettings/cookiepolicy-swift.type.property.md)
  The metadata for the setting that configures Safari’s policy for cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings/cookiepolicy-swift.enum)*