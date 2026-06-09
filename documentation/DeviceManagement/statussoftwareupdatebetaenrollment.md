# StatusSoftwareUpdateBetaEnrollment

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s enrolled beta program.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object StatusSoftwareUpdateBetaEnrollment
```

## Mentions

- [Deploy software updates using declarative management](deploy-software-updates-using-declarative-management.md)

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad |
| Allowed in device enrollment | iOS, Shared iPad |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "softwareupdate": {
        "beta-enrollment": ""
    }
}
```

## Properties

- `softwareupdate.beta-enrollment` (string) *(required)*: The device’s enrolled beta program name, or an empty string if there’s no enrolled beta program.

## See Also

- [object StatusSoftwareUpdateDeviceID](statussoftwareupdatedeviceid.md)
  The status item that reports the device’s software update device ID.
- [object StatusSoftwareUpdateFailureReason](statussoftwareupdatefailurereason.md)
  The status item that reports the device’s software update failure reason.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdateInstallState](statussoftwareupdateinstallstate.md)
  The status item that reports the device’s software update install state.
- [object StatusSoftwareUpdatePendingVersion](statussoftwareupdatependingversion.md)
  The status item that reports the device’s pending software update version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdatebetaenrollment)*