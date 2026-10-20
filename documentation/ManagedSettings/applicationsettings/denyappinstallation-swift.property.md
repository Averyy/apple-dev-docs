# denyAppInstallation

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to prevent the user from installing applications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var denyAppInstallation: Bool? { get set }
```

#### Discussion

If your app doesn’t constrain this setting, the value is `nil`.

## See Also

### Preventing app installation and removal
- [static let denyAppInstallation: SettingMetadata<Bool>](./denyappinstallation-swift.type.property.md)
  The metadata for the setting to prevent app installation.
- [var denyAppRemoval: Bool?](./denyappremoval-swift.property.md)
  A Boolean value that indicates whether to prevent the user from removing applications.
- [static let denyAppRemoval: SettingMetadata<Bool>](./denyappremoval-swift.type.property.md)
  The metadata for the setting to prevent app removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationsettings/denyappinstallation-swift.property)*