# webDomains

**Framework**: ManagedSettings  
**Kind**: property

The metadata for the configuration that specifies websites for the system to shield.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let webDomains: SettingMetadata<Set<WebDomainToken>>
```

#### Discussion

Use `webDomains` to access the metadata for [`webDomains`](shieldsettings/webdomains-swift.property.md). The default value is an empty set.

## See Also

- [var applications: Set<ApplicationToken>?](shieldsettings/applications-swift.property.md)
  Applications for the system to cover with a shielding view.
- [static let applications: SettingMetadata<Set<ApplicationToken>>](shieldsettings/applications-swift.type.property.md)
  The metadata for the configuration that specifies apps for the system to cover with a shielding view.
- [var webDomains: Set<WebDomainToken>?](shieldsettings/webdomains-swift.property.md)
  Websites for the system to cover with a shielding view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/webdomains-swift.type.property)*