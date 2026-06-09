# StatusEnhancedLoggingTimestamp

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s enhanced log collection session timestamp.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
object StatusEnhancedLoggingTimestamp
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
        "timestamp": "2025-05-15T10:30:00Z"
    }
}
```

## Properties

- `enhanced-logging.timestamp` (string): The enhanced log collection session RFC 3339 timestamp that the device reports for the last session status change. The device returns an empty string if there is no session status to report.

## See Also

- [object StatusEnhancedLogging](statusenhancedlogging.md)
  The status item that reports the device’s enhanced log collection session status.
- [object StatusEnhancedLoggingAppleCareToken](statusenhancedloggingapplecaretoken.md)
  The status item that reports the device’s enhanced log collection session AppleCare token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusenhancedloggingtimestamp)*