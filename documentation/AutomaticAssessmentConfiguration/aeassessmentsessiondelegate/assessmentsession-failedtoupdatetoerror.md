# assessmentSession(_:failedToUpdateTo:error:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Tells the delegate that a configuration update failed.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
optional func assessmentSession(_ session: AEAssessmentSession, failedToUpdateTo configuration: AEAssessmentConfiguration, error: any Error)
```

#### Discussion

After you call a session’s [`update(to:)`](aeassessmentsession/update(to:).md) method, the session calls this delegate method if the update fails. If the update succeeds, the session calls [`assessmentSessionDidUpdate(_:)`](aeassessmentsessiondelegate/assessmentsessiondidupdate(_:).md) instead.

## Parameters

- `session`: The session that you attempted to update.
- `configuration`: The configuration that you attempted to update the session with.
- `error`: An error that describes the reason for the failure.

## See Also

- [func assessmentSessionDidUpdate(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidupdate(_:).md)
  Tells the delegate that a configuration update succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsession(_:failedtoupdateto:error:))*