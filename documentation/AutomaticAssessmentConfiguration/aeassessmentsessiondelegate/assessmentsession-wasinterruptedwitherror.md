# assessmentSession(_:wasInterruptedWithError:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Tells the delegate that a system failure interrupted the session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
optional func assessmentSession(_ session: AEAssessmentSession, wasInterruptedWithError error: any Error)
```

#### Discussion

If one or more subsystems fail during a session, the session tells its delegate by calling the [`assessmentSession(_:wasInterruptedWithError:)`](aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:).md) method. If your app receives this callback, immediately stop the assessment, hide all sensitive content, and end the session. Because it might take time for your app to stop the assessment, the session relies on your app to call the [`end()`](aeassessmentsession/end().md) method:

## Parameters

- `session`: The session that failed.
- `error`: An error that provides information about the interruption.

## See Also

- [func assessmentSessionDidBegin(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:).md)
  Tells the delegate that the session failed to start.
- [func assessmentSessionDidEnd(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:))*