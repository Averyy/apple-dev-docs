# assessmentSession(_:failedToBeginWithError:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) assessmentSession:(AEAssessmentSession *) session failedToBeginWithError:(NSError *) error;
```

#### Discussion

After your app calls a session’s [`begin()`](../aeassessmentsession/begin%28%29.md) method, the session asynchronously disables the appropriate system services and then calls its delegate’s [`assessmentSessionDidBegin(_:)`](./assessmentsessiondidbegin%28_%29.md) method. However, if the session fails to start for any reason, it calls the [`assessmentSession(_:failedToBeginWithError:)`](./assessmentsession%28_,failedtobeginwitherror%29.md) method instead. Don’t start any assessments if your app receives this callback.

## Parameters

- `session`: The session that failed to start.
- `error`: An error that provides information about why the session failed.

## See Also

### Responding to session start and stop
- [func assessmentSessionDidBegin(AEAssessmentSession)](./assessmentsessiondidbegin%28_%29.md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](./assessmentsession%28_,wasinterruptedwitherror%29.md)
  Tells the delegate that a system failure interrupted the session.
- [func assessmentSessionDidEnd(AEAssessmentSession)](./assessmentsessiondidend%28_%29.md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:))*