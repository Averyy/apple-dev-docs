# StatusMDMEnrollmentType

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s management enrollment type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
object StatusMDMEnrollmentType
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

```json
{
    "mdm": {
        "enrollment-type": "supervised"
    }
}
```

## Properties

- `mdm.enrollment-type` (string) *(required)*: The device management enrollment type that indicates how the device is enrolled, which has the following possible values: - `none`: Device is not enrolled
- `supervised`: Device is supervised
- `device`: Device enrollment
- `user`: User enrollment

## See Also

- [object StatusMDMIsAwaitingConfiguration](statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmenrollmenttype)*