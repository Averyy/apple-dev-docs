# StatusPasscodeCompliance

**Framework**: Device Management  
**Kind**: dictionary

A status report of passcode compliance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusPasscodeCompliance
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

- `passcode.is-compliant` (boolean) *(required)*: If `true`, the passcode is in compliance with all passcode policies set on the device. If `false`, the passcode isn’t in compliance with one or more passcode policies set on the device. When there are no passcode policies on the device, this value `true`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspasscodecompliance)*