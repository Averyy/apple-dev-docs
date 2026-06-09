# StatusMDMPushToken

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s push token.

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
object StatusMDMPushToken
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
        "push-token": "4A8B3F2E1D9C7B6A5E4D3C2B1A0F9E8D7C6B5A4E3D2C1B0A"
    }
}
```

## Properties

- `mdm.push-token` (string) *(required)*: The device push token that the MDM server uses for Apple Push Notification service messages.

## See Also

- [object StatusMDMEnrollmentType](statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsAwaitingConfiguration](statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmpushtoken)*