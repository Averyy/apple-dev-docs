# assessmentSessionDidUpdate(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Tells the delegate that a configuration update succeeded.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
optional func assessmentSessionDidUpdate(_ session: AEAssessmentSession)
```

#### Discussion

After you call a session’s [`update(to:)`](aeassessmentsession/update(to:).md) method, the session calls this delegate method to indicate a successful update. If the update fails, the session calls [`assessmentSession(_:failedToUpdateTo:error:)`](aeassessmentsessiondelegate/assessmentsession(_:failedtoupdateto:error:).md) instead.

## Parameters

- `session`: The session that received the configuration update.

## See Also

- [func assessmentSession(AEAssessmentSession, failedToUpdateTo: AEAssessmentConfiguration, error: any Error)](aeassessmentsessiondelegate/assessmentsession(_:failedtoupdateto:error:).md)
  Tells the delegate that a configuration update failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsessiondidupdate(_:))*