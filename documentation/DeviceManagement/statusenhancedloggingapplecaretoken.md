# StatusEnhancedLoggingAppleCareToken

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s enhanced log collection session AppleCare token.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
object StatusEnhancedLoggingAppleCareToken
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
        "applecare-token": "ABC123DEF456"
    }
}
```

## Properties

- `enhanced-logging.applecare-token` (string): The current enhanced log collection session AppleCare token. The device returns an empty string if there’s no session status to report.

## See Also

- [object StatusEnhancedLoggingStatus](statusenhancedloggingstatus.md)
  The status item that reports the device’s enhanced log collection session status.
- [object StatusEnhancedLoggingTimestamp](statusenhancedloggingtimestamp.md)
  The status item that reports the device’s enhanced log collection session timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusenhancedloggingapplecaretoken)*