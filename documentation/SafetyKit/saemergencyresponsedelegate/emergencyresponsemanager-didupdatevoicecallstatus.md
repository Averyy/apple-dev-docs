# emergencyResponseManager(_:didUpdateVoiceCallStatus:)

**Framework**: SafetyKit  
**Kind**: method  
**Required**: Yes

Provides the voice call status to the delegate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
optional func emergencyResponseManager(_ emergencyResponseManager: SAEmergencyResponseManager, didUpdateVoiceCallStatus voiceCallStatus: SAEmergencyResponseManager.VoiceCallStatus)
```

#### Discussion

A voice call to the desired contact can occur when running in the foreground or background within a limited time window of a Crash Detection event. Use this delegate method to monitor the status of the requested voice call.

## Parameters

- `emergencyResponseManager`: The emergency response object responsible for the status update.
- `voiceCallStatus`: The status of the voice call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saemergencyresponsedelegate/emergencyresponsemanager(_:didupdatevoicecallstatus:))*