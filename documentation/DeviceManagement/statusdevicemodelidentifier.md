# StatusDeviceModelIdentifier

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s hardware model identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusDeviceModelIdentifier
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

```json
{
    "device": {
        "model": {
            "identifier": "iPhone14,5"
        }
    }
}
```

## Properties

- `device.model.identifier` (string) *(required)*: A two-part string that specifies the device’s model. The first part specifies device’s model family, and the second part specifies the model’s version. The model’s version is a comma-separated number where the first part of the number is the version, and the second part is a variant, such as `MacBookPro15,1` or `iPhone13,2`.

## See Also

- [object StatusDeviceBatteryHealth](statusdevicebatteryhealth.md)
  The status item that reports the device’s battery health.
- [object StatusDeviceModelFamily](statusdevicemodelfamily.md)
  The status item that reports the device’s hardware model family.
- [object StatusDeviceModelMarketingName](statusdevicemodelmarketingname.md)
  The status item that reports the device’s model marketing name.
- [object StatusDeviceModelNumber](statusdevicemodelnumber.md)
  The status item that reports the device’s hardware number.
- [object StatusDeviceOperatingSystemBuildVersion](statusdeviceoperatingsystembuildversion.md)
  The status item that reports the device’s operating system build version.
- [object StatusDeviceOperatingSystemFamily](statusdeviceoperatingsystemfamily.md)
  The status item that reports the device’s operating system family.
- [object StatusDeviceOperatingSystemMarketingName](statusdeviceoperatingsystemmarketingname.md)
  The status item that reports the device’s operating system marketing name.
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  The status item that reports the device’s operating system supplemental build version and Background Security Improvement version.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  The status item that reports the device’s operating system Background Security Improvement version.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  The status item that reports the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  The status item that reports the device’s serial number.
- [object StatusDeviceSystemHealth](statusdevicesystemhealth.md)
  The status item that reports the device’s system health.
- [object StatusDeviceUDID](statusdeviceudid.md)
  The status item that reports the device’s UDID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicemodelidentifier)*