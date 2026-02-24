# StatusPasscodeIsPresent

**Framework**: Device Management  
**Kind**: dictionary

A status report of the passcode on the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusPasscodeIsPresent
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, Shared iPad, visionOS, watchOS |
| Allowed in system scope | iOS, Shared iPad, visionOS, watchOS |
| Allowed in user scope | Shared iPad |

## Properties

- `passcode.is-present` (boolean) *(required)*: If `true`, a passcode is present on the device. If `false`, a passcode isn’t present on the device. When a passcode is present, the specific attributes of the passcode, such as length or number of complex characters, aren’t reported. Instead, use the `passcode.is-compliant` status item to verify that the passcode complies with all passcode policies set on the device.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspasscodeispresent)*