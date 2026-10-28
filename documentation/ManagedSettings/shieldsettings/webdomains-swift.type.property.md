# webDomains

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Type Property

The metadata for the configuration that specifies websites for the system to shield.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let webDomains: SettingMetadata<Set<WebDomainToken>>
```

## Discussion

Use `webDomains` to access the metadata for [`webDomains`](./webdomains-swift.property.md). The default value is an empty set.

## See Also

### Blocking apps and websites
- [var applications: Set<ApplicationToken>?](./applications-swift.property.md)
  Applications for the system to cover with a shielding view.
- [static let applications: SettingMetadata<Set<ApplicationToken>>](./applications-swift.type.property.md)
  The metadata for the configuration that specifies apps for the system to cover with a shielding view.
- [var webDomains: Set<WebDomainToken>?](./webdomains-swift.property.md)
  Websites for the system to cover with a shielding view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/webdomains-swift.type.property)*