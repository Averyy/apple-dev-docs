# StatusSoftwareUpdateDeviceID

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s software update device ID.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.4+
- visionOS 26.4+

## Declaration

```swift
object StatusSoftwareUpdateDeviceID
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "softwareupdate": {
        "device-id": "iPhone14,3"
    }
}
```

## Properties

- `softwareupdate.device-id` (string) *(required)*: The device identifier to use when looking up available software updates via `https://gdmf.apple.com/v2/pmv`.

## See Also

- [object StatusSoftwareUpdateBetaEnrollment](statussoftwareupdatebetaenrollment.md)
  The status item that reports the device’s enrolled beta program.
- [object StatusSoftwareUpdateFailureReason](statussoftwareupdatefailurereason.md)
  The status item that reports the device’s software update failure reason.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdateInstallState](statussoftwareupdateinstallstate.md)
  The status item that reports the device’s software update install state.
- [object StatusSoftwareUpdatePendingVersion](statussoftwareupdatependingversion.md)
  The status item that reports the device’s pending software update version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdatedeviceid)*