# StatusEnhancedLoggingStatus

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s enhanced log collection session status.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
object StatusEnhancedLoggingStatus
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad, tvOS |
| Allowed in user scope | macOS |

##### Status Item Example

```json
{
    "enhanced-logging": {
        "status": "collecting"
    }
}
```

## Properties

- `enhanced-logging.status` (string) *(required)*: The enhanced log collection session status, which has the following values: - `none`: The device has never run an enhanced log collection session.
- `waiting-for-consent`: The device is waiting for the user to consent to the enhanced log collection.
- `collecting`: The enhanced log collection is in progress.
- `follow-up-question`: The device is waiting for follow-up response from the user.
- `upload-consent`: The device is waiting for the user to approve upload of the enhanced logs.
- `uploading`: The device is uploading the enhanced logs.
- `finished`: The device completed the enhanced log collection session.
- `failed`: The device failed to complete the enhanced log collection session.
- `cancelled` - The device management service cancelled the enhanced log collection session.
- `declined` - The user declined the enhanced log collection session.

## See Also

- [object StatusEnhancedLoggingAppleCareToken](statusenhancedloggingapplecaretoken.md)
  The status item that reports the device’s enhanced log collection session AppleCare token.
- [object StatusEnhancedLoggingTimestamp](statusenhancedloggingtimestamp.md)
  The status item that reports the device’s enhanced log collection session timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusenhancedloggingstatus)*