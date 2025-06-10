# StatusAppManagedList

**Framework**: Device Management  
**Kind**: dictionary

The device’s declarative managed apps.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 26.0+ (Beta)
- visionOS 2.4+

## Declaration

```swift
object StatusAppManagedList
```

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | macOS |

##### Reason Codes

- `Error.AppStoreDisabled`: The App Store is disabled.
- `Error.DownloadFailed`: The app download failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last download failure.
- `Error.DuplicateConfiguredApp`: The app is already being managed.
- `Error.InstallFailed`: The app install failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last install failure.
- `Error.InvalidAppID`: The app id could not be found.
- `Error.InvalidCodeSignature`: The code signature of the app does not match the composed identifier, and the app cannot be managed.
- `Error.IsSystemApp`: The app is a system app that cannot be managed.
- `Error.LicenseNotFound`: A license for the app was not available.
- `Error.NotAnApp`: The downloaded data is not a valid app.
- `Error.NotSupported`: The app is not supported on this device.
- `Error.UnmanagedAppAlreadyInstalled`: An unmanaged app is already installed and cannot be managed.
- `Error.UserRejected`: The user rejected management of the app.
- `Info.UpdateAvailable`: An update is available for the app.
- `Error.UpdateFailed`: The app update failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last update failure.

## Topics

### Objects
- [object StatusAppManagedListAppObject](statusappmanagedlistappobject.md)
  A dictionary that describes a declarative managed app.

## See Also

- [object StatusReport](statusreport.md)
- [object StatusDeviceBatteryHealth](statusdevicebatteryhealth.md)
  The device’s battery health.
- [object StatusDeviceModelFamily](statusdevicemodelfamily.md)
  A status report of the device’s hardware family.
- [object StatusDeviceModelIdentifier](statusdevicemodelidentifier.md)
  A status report of the device’s hardware identifier.
- [object StatusDeviceModelMarketingName](statusdevicemodelmarketingname.md)
  A status report of the device’s marketing name.
- [object StatusDeviceModelNumber](statusdevicemodelnumber.md)
  A status report of the device’s hardware number.
- [object StatusDeviceOperatingSystemBuildVersion](statusdeviceoperatingsystembuildversion.md)
  A status report of the device’s software build identifier.
- [object StatusDeviceOperatingSystemFamily](statusdeviceoperatingsystemfamily.md)
  A status report of the device’s operating system family.
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  A status report of the device’s operating system supplemental build identifier.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  A status report of the device’s operating system’s rapid security response identifier.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  A status report of the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  A status report of the device’s serial number.
- [object StatusDeviceUDID](statusdeviceudid.md)
  A status report of the device’s UDID.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The enabled status of the File Vault.
- [object StatusManagementClientCapabilities](statusmanagementclientcapabilities.md)
  A status report of the client’s protocol capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlist)*