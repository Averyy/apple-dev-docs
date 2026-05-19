# SAEmergencyResponseDelegate

**Framework**: SafetyKit  
**Kind**: protocol

The interface for receiving updates about a requested emergency response action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
protocol SAEmergencyResponseDelegate : NSObjectProtocol
```

## Topics

### Receiving voice call status
- [func emergencyResponseManager(SAEmergencyResponseManager, didUpdateVoiceCallStatus: SAEmergencyResponseManager.VoiceCallStatus)](saemergencyresponsedelegate/emergencyresponsemanager(_:didupdatevoicecallstatus:).md)
  Provides the voice call status to the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SAEmergencyResponseManager](saemergencyresponsemanager.md)
  Provides actions in response to a Crash Detection event.
- [SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsedelegate)*