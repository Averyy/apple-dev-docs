# SAEmergencyResponseManager.VoiceCallStatus

**Framework**: SafetyKit  
**Kind**: enum

An enumeration that defines the status of a requested voice call.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
enum VoiceCallStatus
```

## Topics

### Determining call status
- [SAEmergencyResponseManager.VoiceCallStatus.active](saemergencyresponsemanager/voicecallstatus/active.md)
  The system successfully placed a call to the desired contact and that call is currently active.
- [SAEmergencyResponseManager.VoiceCallStatus.dialing](saemergencyresponsemanager/voicecallstatus/dialing.md)
  The system is dialing the desired contact.
- [SAEmergencyResponseManager.VoiceCallStatus.disconnected](saemergencyresponsemanager/voicecallstatus/disconnected.md)
  The voice call to the desired contact disconnected.
- [SAEmergencyResponseManager.VoiceCallStatus.failed](saemergencyresponsemanager/voicecallstatus/failed.md)
  The voice call failed to connect to the desired contact.
### Initializers
- [init?(rawValue: Int)](saemergencyresponsemanager/voicecallstatus/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](saemergencyresponsemanager/voicecallstatus/equatable-implementations.md)
- [RawRepresentable Implementations](saemergencyresponsemanager/voicecallstatus/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func dialVoiceCall(toPhoneNumber: String, completionHandler: (Bool, (any Error)?) -> Void)](saemergencyresponsemanager/dialvoicecall(tophonenumber:completionhandler:).md)
  Request the system to dial a voice call on behalf of someone involved in a crash.
- [var delegate: (any SAEmergencyResponseDelegate)?](saemergencyresponsemanager/delegate.md)
  The object that receives voice call status updates and requested emergency response actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager/voicecallstatus)*