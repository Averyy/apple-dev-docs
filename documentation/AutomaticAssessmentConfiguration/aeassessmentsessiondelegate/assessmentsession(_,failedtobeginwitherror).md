# assessmentSession(_:failedToBeginWithError:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Tells the delegate that the session failed to start.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
optional func assessmentSession(_ session: AEAssessmentSession, failedToBeginWithError error: any Error)
```

#### Discussion

After your app calls a session’s [`begin()`](aeassessmentsession/begin().md) method, the session asynchronously disables the appropriate system services and then calls its delegate’s [`assessmentSessionDidBegin(_:)`](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md) method. However, if the session fails to start for any reason, it calls the [`assessmentSession(_:failedToBeginWithError:)`](aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:).md) method instead. Don’t start any assessments if your app receives this callback.

## Parameters

- `session`: The session that failed to start.
- `error`: An error that provides information about why the session failed.

## See Also

- [func assessmentSessionDidBegin(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:).md)
  Tells the delegate that a system failure interrupted the session.
- [func assessmentSessionDidEnd(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:))*