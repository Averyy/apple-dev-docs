# SAEmergencyResponseDelegate

**Framework**: SafetyKit  
**Kind**: protocol  
**Role**: Protocol

The interface for receiving updates about a requested emergency response action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
protocol SAEmergencyResponseDelegate : NSObjectProtocol
```

```objc
@protocol SAEmergencyResponseDelegate <NSObject>
```

## Topics

### Receiving voice call status
- [func emergencyResponseManager(SAEmergencyResponseManager, didUpdateVoiceCallStatus: SAEmergencyResponseManager.VoiceCallStatus)](./saemergencyresponsedelegate/emergencyresponsemanager%28_,didupdatevoicecallstatus%29.md)
  Provides the voice call status to the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to a crash
- [class SAEmergencyResponseManager](./saemergencyresponsemanager.md)
  Provides actions in response to a Crash Detection event.
- [SACrashDetectionEvent.Response](./sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsedelegate)*