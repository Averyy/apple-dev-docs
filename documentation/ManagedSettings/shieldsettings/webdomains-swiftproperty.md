# webDomains

**Framework**: ManagedSettings  
**Kind**: property

Websites for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var webDomains: Set<WebDomainToken>? { get set }
```

#### Discussion

When the user visits a website in this list of domains, the system calls your extension that customizes the shield’s appearance. When the user taps on a button the shield displays, the system calls your extension that handles user actions. If your app doesn’t provide a list of domains to shield, this value is `nil`. Your app can shield up to 50 web domain tokens at once.

## See Also

- [var applications: Set<ApplicationToken>?](shieldsettings/applications-swift.property.md)
  Applications for the system to cover with a shielding view.
- [static let applications: SettingMetadata<Set<ApplicationToken>>](shieldsettings/applications-swift.type.property.md)
  The metadata for the configuration that specifies apps for the system to cover with a shielding view.
- [static let webDomains: SettingMetadata<Set<WebDomainToken>>](shieldsettings/webdomains-swift.type.property.md)
  The metadata for the configuration that specifies websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/webdomains-swift.property)*