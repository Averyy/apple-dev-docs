# denyAppInstallation

**Framework**: ManagedSettings  
**Kind**: property

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

- [static let denyAppInstallation: SettingMetadata<Bool>](applicationsettings/denyappinstallation-swift.type.property.md)
  The metadata for the setting to prevent app installation.
- [var denyAppRemoval: Bool?](applicationsettings/denyappremoval-swift.property.md)
  A Boolean value that indicates whether to prevent the user from removing applications.
- [static let denyAppRemoval: SettingMetadata<Bool>](applicationsettings/denyappremoval-swift.type.property.md)
  The metadata for the setting to prevent app removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationsettings/denyappinstallation-swift.property)*