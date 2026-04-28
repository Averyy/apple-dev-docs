# StatusDeviceBatteryHealth

**Framework**: Device Management  
**Kind**: dictionary

The device’s battery health.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusDeviceBatteryHealth
```

#### Discussion

For more information about battery health, see the following support articles:

- [`iPhone devices`](https://developer.apple.comhttps://support.apple.com/101575)
- [`iPad devices`](https://developer.apple.comhttps://support.apple.com/117759)
- [`macOS devices`](https://developer.apple.comhttps://support.apple.com/108376)

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad |
| Allowed in device enrollment | iOS, Shared iPad |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | iOS, macOS, Shared iPad |
| Allowed in system scope | iOS, macOS, Shared iPad |
| Allowed in user scope | NA |

## Properties

- `device.power.battery-health` (string) *(required)*: The battery health status, which has the following values: - `non-genuine`: The battery isn’t a genuine Apple battery.
- `normal`: The battery is operating normally.
- `service-recommended`: The system recommends battery service.
- `unknown`: The system couldn’t determine battery health information.
- `unsupported`: The device doesn’t support battery health reporting. Available in iOS 17 and later on iPhone, iPadOS 18.4 and later on supported iPad models, and macOS 14.4 and later on a Mac with Apple silicon.

## See Also

- [object StatusReport](statusreport.md)
- [object StatusAppManagedList](statusappmanagedlist.md)
  The device’s declarative managed apps.
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
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The enabled status of the File Vault.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicebatteryhealth)*