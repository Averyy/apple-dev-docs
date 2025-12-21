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
### Operators
- [static func < (SafariSettings.CookiePolicy, SafariSettings.CookiePolicy) -> Bool](safarisettings/cookiepolicy-swift.enum/_(_:_:).md)
  Returns a Boolean value that indicates whether the value of the first argument is less than that of the second argument.

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