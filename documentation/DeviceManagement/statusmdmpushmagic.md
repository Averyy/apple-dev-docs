# StatusMDMPushMagic

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s push magic value.

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
object StatusMDMPushMagic
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
        "push-magic": "3B5D81A2-9F4E-4B7C-A8D6-1E2F3A4B5C6D"
    }
}
```

## Properties

- `mdm.push-magic` (string) *(required)*: The push magic value that the device expects the MDM server to include in Apple Push Notification service messages.

## See Also

- [object StatusMDMEnrollmentType](statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsAwaitingConfiguration](statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushToken](statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmpushmagic)*