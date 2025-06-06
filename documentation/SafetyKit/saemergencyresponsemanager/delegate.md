# delegate

**Framework**: SafetyKit  
**Kind**: property

The object that receives voice call status updates and requested emergency response actions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
weak var delegate: (any SAEmergencyResponseDelegate)? { get set }
```

## See Also

- [SAEmergencyResponseManager.VoiceCallStatus](saemergencyresponsemanager/voicecallstatus.md)
  An enumeration that defines the status of a requested voice call.
- [func dialVoiceCall(toPhoneNumber: String, completionHandler: (Bool, (any Error)?) -> Void)](saemergencyresponsemanager/dialvoicecall(tophonenumber:completionhandler:).md)
  Request the system to dial a voice call on behalf of someone involved in a crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager/delegate)*