# StatusSoftwareUpdateInstallState

**Framework**: Device Management  
**Kind**: dictionary

A status report of the software update install state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusSoftwareUpdateInstallState
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | NA |

## Properties

- `softwareupdate.install-state` (string) *(required)*: The software update install status, which has the following values: - `none`: There’s no software update pending, and any previous software update succeeded.
- `waiting’: A software update is waiting to start.
- `downloading`: The system is downloading data for a software update.
- `prepared`: The system prepared the software update and it’s ready for installation.
- `installing`: The system is installing the software update.
- `failed`: The software update failed.

## See Also

- [object StatusReport](statusreport.md)
- [object StatusAppManagedList](statusappmanagedlist.md)
  The device’s declarative managed apps.
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
- [object StatusDeviceOperatingSystemMarketingName](statusdeviceoperatingsystemmarketingname.md)
  A status report of the device’s operating system marketing name.
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  A status report of the device’s operating system supplemental build identifier.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  A status report of the device’s operating system’s Background Security Improvement identifier.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  A status report of the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  A status report of the device’s serial number.
- [object StatusDeviceUDID](statusdeviceudid.md)
  A status report of the device’s UDID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdateinstallstate)*