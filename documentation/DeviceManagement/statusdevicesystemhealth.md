# StatusDeviceSystemHealth

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s system health.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
object StatusDeviceSystemHealth
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "device": {
        "system": {
            "health": {
                "Camera": "ok",
                "Display": "ok",
                "FaceID": "ok"
            }
        }
    }
}
```

## Topics

### Objects
- [object StatusDeviceSystemHealthDeviceSystemHealthObject](statusdevicesystemhealthdevicesystemhealthobject.md)
  A dictionary where each key represents a hardware component name and each value is a string indicating the component’s health status, which has the following values:

## Properties

- `device.system.health` (StatusDeviceSystemHealthDeviceSystemHealthObject) *(required)*: A dictionary where each key represents a hardware component name and each value is a string indicating the component’s health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `non-genuine`: The component isn’t a genuine Apple component. Not all keys are supported on each device. The dictionary includes only components that are present and reportable on the device.

## See Also

- [object StatusDeviceBatteryHealth](statusdevicebatteryhealth.md)
  The status item that reports the device’s battery health.
- [object StatusDeviceModelFamily](statusdevicemodelfamily.md)
  The status item that reports the device’s hardware model family.
- [object StatusDeviceModelIdentifier](statusdevicemodelidentifier.md)
  The status item that reports the device’s hardware model identifier.
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
- [object StatusDeviceUDID](statusdeviceudid.md)
  The status item that reports the device’s UDID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicesystemhealth)*