# StatusSoftwareUpdateInstallState

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s software update install state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object StatusSoftwareUpdateInstallState
```

## Mentions

- [Phases of software update enforcement](phases-of-software-update-enforcement.md)
- [Deploy software updates using declarative management](deploy-software-updates-using-declarative-management.md)

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
        "install-state": "none"
    }
}
```

## Properties

- `softwareupdate.install-state` (string) *(required)*: The software update install status, which has the following values: - `none`: There’s no software update pending, and any previous software update succeeded.
- `downloading`: The system is downloading data for a software update.
- `prepared`: The system prepared the software update and it’s ready for installation.
- `installing`: The system is installing the software update.
- `failed`: The software update failed.

## See Also

- [object StatusSoftwareUpdateBetaEnrollment](statussoftwareupdatebetaenrollment.md)
  The status item that reports the device’s enrolled beta program.
- [object StatusSoftwareUpdateDeviceID](statussoftwareupdatedeviceid.md)
  The status item that reports the device’s software update device ID.
- [object StatusSoftwareUpdateFailureReason](statussoftwareupdatefailurereason.md)
  The status item that reports the device’s software update failure reason.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdatePendingVersion](statussoftwareupdatependingversion.md)
  The status item that reports the device’s pending software update version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdateinstallstate)*