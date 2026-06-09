# StatusDeviceBatteryHealth

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s battery health.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.4+

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
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, macOS, Shared iPad |
| Allowed in system scope | iOS, macOS, Shared iPad |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "device": {
        "power": {
            "battery-health": "normal"
        }
    }
}
```

## Properties

- `device.power.battery-health` (string) *(required)*: The battery health status, which has the following values: - `non-genuine`: The battery isn’t a genuine Apple battery.
- `normal`: The battery is operating normally.
- `service-recommended`: The system recommends battery service.
- `unknown`: The system couldn’t determine battery health information.
- `unsupported`: The device doesn’t support battery health reporting. Supported on iPhones, specific iPad models, and Mac computers with Apple silicon.

## See Also

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
- [object StatusDeviceSystemHealth](statusdevicesystemhealth.md)
  The status item that reports the device’s system health.
- [object StatusDeviceUDID](statusdeviceudid.md)
  The status item that reports the device’s UDID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicebatteryhealth)*