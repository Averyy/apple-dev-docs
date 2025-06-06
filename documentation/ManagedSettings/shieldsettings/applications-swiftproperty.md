# applications

**Framework**: ManagedSettings  
**Kind**: property

Applications for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var applications: Set<ApplicationToken>? { get set }
```

#### Discussion

When the user launches an application in this set, the system calls your extension that customizes the shield’s appearance. When the user taps on a button the shield displays, the system calls your extension that handles user actions. If your app doesn’t provide a list of applications to shield, this value is `nil`. Your app can shield up to 50 application tokens at once.

## See Also

- [static let applications: SettingMetadata<Set<ApplicationToken>>](shieldsettings/applications-swift.type.property.md)
  The metadata for the configuration that specifies apps for the system to cover with a shielding view.
- [var webDomains: Set<WebDomainToken>?](shieldsettings/webdomains-swift.property.md)
  Websites for the system to cover with a shielding view.
- [static let webDomains: SettingMetadata<Set<WebDomainToken>>](shieldsettings/webdomains-swift.type.property.md)
  The metadata for the configuration that specifies websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/applications-swift.property)*