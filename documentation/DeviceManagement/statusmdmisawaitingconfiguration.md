# StatusMDMIsAwaitingConfiguration

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device management awaiting configuration state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object StatusMDMIsAwaitingConfiguration
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

```json
{
    "mdm": {
        "is-awaiting-configuration": false
    }
}
```

## Properties

- `mdm.is-awaiting-configuration` (boolean) *(required)*: If `true`, the device is awaiting configuration from the MDM server.

## See Also

- [object StatusMDMEnrollmentType](statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsReturnToService](statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmisawaitingconfiguration)*