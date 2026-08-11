# StatusSoftwareUpdateFailureReason

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s software update failure reason.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object StatusSoftwareUpdateFailureReason
```

## Mentions

- [Deploying software updates using declarative management](deploying-software-updates-using-declarative-management.md)
- [Phases of software update enforcement](phases-of-software-update-enforcement.md)

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
        "failure-reason": {
            "count": 0
        }
    }
}
```

## Topics

### Objects
- [object StatusSoftwareUpdateFailureReasonDictionaryObject](statussoftwareupdatefailurereasondictionaryobject.md)
  Details about a software update failure.

## Properties

- `softwareupdate.failure-reason` (StatusSoftwareUpdateFailureReasonDictionaryObject) *(required)*: Details about a software update failure.

## See Also

- [object StatusSoftwareUpdateBetaEnrollment](statussoftwareupdatebetaenrollment.md)
  The status item that reports the device’s enrolled beta program.
- [object StatusSoftwareUpdateDeviceID](statussoftwareupdatedeviceid.md)
  The status item that reports the device’s software update device ID.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdateInstallState](statussoftwareupdateinstallstate.md)
  The status item that reports the device’s software update install state.
- [object StatusSoftwareUpdatePendingVersion](statussoftwareupdatependingversion.md)
  The status item that reports the device’s pending software update version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdatefailurereason)*