# assessmentSessionDidBegin(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Tells the delegate that the session started.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
optional func assessmentSessionDidBegin(_ session: AEAssessmentSession)
```

#### Discussion

After your app calls a session’s [`begin()`](aeassessmentsession/begin().md) method, the session asynchronously disables the appropriate system services and then calls its delegate’s [`assessmentSessionDidBegin(_:)`](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md) method. Only after receiving this callback can you be sure that it’s safe to start an assessment. If the session fails to start for any reason, you receive a call to the [`assessmentSession(_:failedToBeginWithError:)`](aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:).md) method instead.

## Parameters

- `session`: The session that started.

## See Also

- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:).md)
  Tells the delegate that the session failed to start.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:).md)
  Tells the delegate that a system failure interrupted the session.
- [func assessmentSessionDidEnd(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsessiondidbegin(_:))*