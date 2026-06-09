# StatusMDMIsReturnToService

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s return to service with app preservation state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object StatusMDMIsReturnToService
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad, visionOS |
| Allowed in user scope | Shared iPad |

##### Status Item Example

```json
{
    "mdm": {
        "is-return-to-service": false
    }
}
```

## Properties

- `mdm.is-return-to-service` (boolean) *(required)*: If `true`, the device is using the return to service with app preservation mode.

## See Also

- [object StatusMDMEnrollmentType](statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsAwaitingConfiguration](statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmisreturntoservice)*