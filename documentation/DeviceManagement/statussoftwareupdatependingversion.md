# StatusSoftwareUpdatePendingVersion

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s pending software update version.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object StatusSoftwareUpdatePendingVersion
```

## Mentions

- [Deploying software updates using declarative management](deploying-software-updates-using-declarative-management.md)

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
        "pending-version": {
            "os-version": "27.1",
            "build-version": "24B32"
        }
    }
}
```

## Topics

### Objects
- [object StatusSoftwareUpdatePendingVersionDictionaryObject](statussoftwareupdatependingversiondictionaryobject.md)
  A dictionary that contains the build and OS versions of the software update that’s pending on the device.

## Properties

- `softwareupdate.pending-version` (StatusSoftwareUpdatePendingVersionDictionaryObject) *(required)*: A dictionary that contains the build and OS versions of the software update that’s pending on the device.

## See Also

- [object StatusSoftwareUpdateBetaEnrollment](statussoftwareupdatebetaenrollment.md)
  The status item that reports the device’s enrolled beta program.
- [object StatusSoftwareUpdateDeviceID](statussoftwareupdatedeviceid.md)
  The status item that reports the device’s software update device ID.
- [object StatusSoftwareUpdateFailureReason](statussoftwareupdatefailurereason.md)
  The status item that reports the device’s software update failure reason.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdateInstallState](statussoftwareupdateinstallstate.md)
  The status item that reports the device’s software update install state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdatependingversion)*