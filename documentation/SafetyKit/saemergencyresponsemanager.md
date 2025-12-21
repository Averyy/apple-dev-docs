# SAEmergencyResponseManager

**Framework**: SafetyKit  
**Kind**: class

Provides actions in response to a Crash Detection event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
class SAEmergencyResponseManager
```

#### Overview

Use the manager to place a voice call to an emergency contact upon receipt of a Crash Detection event. Provide an object that adopts [`SAEmergencyResponseDelegate`](saemergencyresponsedelegate.md) in order to respond to the status of the voice call.

## Topics

### Placing a voice call
- [SAEmergencyResponseManager.VoiceCallStatus](saemergencyresponsemanager/voicecallstatus.md)
  An enumeration that defines the status of a requested voice call.
- [func dialVoiceCall(toPhoneNumber: String, completionHandler: (Bool, (any Error)?) -> Void)](saemergencyresponsemanager/dialvoicecall(tophonenumber:completionhandler:).md)
  Request the system to dial a voice call on behalf of someone involved in a crash.
- [var delegate: (any SAEmergencyResponseDelegate)?](saemergencyresponsemanager/delegate.md)
  The object that receives voice call status updates and requested emergency response actions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SAEmergencyResponseDelegate](saemergencyresponsedelegate.md)
  The interface for receiving updates about a requested emergency response action.
- [SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager)*