# cookiePolicy

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

Defines the conditions under which Safari accepts cookies.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var cookiePolicy: SafariSettings.CookiePolicy? { get set }
```

## Discussion

The value is `nil` if this setting has not been applied.

## See Also

### Specifying a cookie policy
- [static let cookiePolicy: SettingMetadata<SafariSettings.CookiePolicy>](./cookiepolicy-swift.type.property.md)
  The metadata for the setting that configures Safari’s policy for cookies.
- [SafariSettings.CookiePolicy](./cookiepolicy-swift.enum.md)
  The conditions under which Safari accepts cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings/cookiepolicy-swift.property)*