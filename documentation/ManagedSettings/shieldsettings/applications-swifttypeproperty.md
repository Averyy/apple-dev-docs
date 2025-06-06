# applications

**Framework**: ManagedSettings  
**Kind**: property

The metadata for the configuration that specifies apps for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let applications: SettingMetadata<Set<ApplicationToken>>
```

#### Discussion

The default value is an empty set.

## See Also

- [var applications: Set<ApplicationToken>?](shieldsettings/applications-swift.property.md)
  Applications for the system to cover with a shielding view.
- [var webDomains: Set<WebDomainToken>?](shieldsettings/webdomains-swift.property.md)
  Websites for the system to cover with a shielding view.
- [static let webDomains: SettingMetadata<Set<WebDomainToken>>](shieldsettings/webdomains-swift.type.property.md)
  The metadata for the configuration that specifies websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/applications-swift.type.property)*