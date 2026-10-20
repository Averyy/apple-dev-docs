# SAEmergencyResponseManager.VoiceCallStatus

**Framework**: SafetyKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that defines the status of a requested voice call.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
enum VoiceCallStatus
```

```c
enum SAEmergencyResponseManagerVoiceCallStatus : NSInteger;
```

## Topics

### Determining call status
- [SAEmergencyResponseManager.VoiceCallStatus.active](./voicecallstatus/active.md)
  The system successfully placed a call to the desired contact and that call is currently active.
- [SAEmergencyResponseManager.VoiceCallStatus.dialing](./voicecallstatus/dialing.md)
  The system is dialing the desired contact.
- [SAEmergencyResponseManager.VoiceCallStatus.disconnected](./voicecallstatus/disconnected.md)
  The voice call to the desired contact disconnected.
- [SAEmergencyResponseManager.VoiceCallStatus.failed](./voicecallstatus/failed.md)
  The voice call failed to connect to the desired contact.
### Initializers
- [init?(rawValue: Int)](./voicecallstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Placing a voice call
- [func dialVoiceCall(toPhoneNumber: String, completionHandler: (Bool, (any Error)?) -> Void)](./dialvoicecall%28tophonenumber,completionhandler%29.md)
  Request the system to dial a voice call on behalf of someone involved in a crash.
- [var delegate: (any SAEmergencyResponseDelegate)?](./delegate.md)
  The object that receives voice call status updates and requested emergency response actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager/voicecallstatus)*