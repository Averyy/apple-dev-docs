# SafariSettings.CookiePolicy

**Framework**: Managed Settings  
**Kind**: enum  
**Role**: Enumeration

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

### Accepting cookies
- [SafariSettings.CookiePolicy.always](./cookiepolicy-swift.enum/always.md)
  A policy that indicates the device accepts cookies from all websites.
- [SafariSettings.CookiePolicy.currentWebsite](./cookiepolicy-swift.enum/currentwebsite.md)
  A policy that indicates the device only accepts cookies from the current website.
- [SafariSettings.CookiePolicy.never](./cookiepolicy-swift.enum/never.md)
  A policy that indicates the device doesn’t accept cookies from any website.
- [SafariSettings.CookiePolicy.visitedWebsites](./cookiepolicy-swift.enum/visitedwebsites.md)
  A policy that indicates the device only accepts cookies from websites in the user’s browsing history.
### Operators
- [static func < (SafariSettings.CookiePolicy, SafariSettings.CookiePolicy) -> Bool](./cookiepolicy-swift.enum/op%28_,_%29.md)
  Returns a Boolean value that indicates whether the value of the first argument is less than that of the second argument.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Specifying a cookie policy
- [var cookiePolicy: SafariSettings.CookiePolicy?](./cookiepolicy-swift.property.md)
  Defines the conditions under which Safari accepts cookies.
- [static let cookiePolicy: SettingMetadata<SafariSettings.CookiePolicy>](./cookiepolicy-swift.type.property.md)
  The metadata for the setting that configures Safari’s policy for cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings/cookiepolicy-swift.enum)*