# StatusEnhancedLoggingNonInteractiveEligibility

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The status item that reports whether the device is eligible to run a non-interactive enhanced log collection session.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+

## Declaration

```
object StatusEnhancedLoggingNonInteractiveEligibility
```

#### Discussion

##### Status item availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad, tvOS |
| Allowed in user scope | macOS |

##### Status item example

```json
{
    "enhanced-logging": {
        "noninteractive-eligibility": true
    }
}
```

## Properties

- `enhanced-logging.noninteractive-eligibility` (boolean) *(required)*: If `true`, the device is eligible to run a non-interactive enhanced log collection session.

## See Also

### Enhanced logging items
- [object StatusEnhancedLoggingStatus](./statusenhancedloggingstatus.md)
  The status item that reports the device’s enhanced log collection session status.
- [object StatusEnhancedLoggingAppleCareToken](./statusenhancedloggingapplecaretoken.md)
  The status item that reports the device’s enhanced log collection session AppleCare token.
- [object StatusEnhancedLoggingTimestamp](./statusenhancedloggingtimestamp.md)
  The status item that reports the device’s enhanced log collection session timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusenhancedloggingnoninteractiveeligibility)*