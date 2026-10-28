# assessmentSessionDidBegin(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) assessmentSessionDidBegin:(AEAssessmentSession *) session;
```

## Discussion

After your app calls a session’s [`begin()`](../aeassessmentsession/begin%28%29.md) method, the session asynchronously disables the appropriate system services and then calls its delegate’s [`assessmentSessionDidBegin(_:)`](./assessmentsessiondidbegin%28_%29.md) method. Only after receiving this callback can you be sure that it’s safe to start an assessment. If the session fails to start for any reason, you receive a call to the [`assessmentSession(_:failedToBeginWithError:)`](./assessmentsession%28_,failedtobeginwitherror%29.md) method instead.

## Parameters

- `session`: The session that started.

## See Also

### Responding to session start and stop
- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](./assessmentsession%28_,failedtobeginwitherror%29.md)
  Tells the delegate that the session failed to start.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](./assessmentsession%28_,wasinterruptedwitherror%29.md)
  Tells the delegate that a system failure interrupted the session.
- [func assessmentSessionDidEnd(AEAssessmentSession)](./assessmentsessiondidend%28_%29.md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsessiondidbegin(_:))*