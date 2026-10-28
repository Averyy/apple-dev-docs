# assessmentSessionDidEnd(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the session ended.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
optional func assessmentSessionDidEnd(_ session: AEAssessmentSession)
```

```objc
- (void) assessmentSessionDidEnd:(AEAssessmentSession *) session;
```

## Discussion

After your app calls a session’s [`end()`](../aeassessmentsession/end%28%29.md) method, the system asynchronously restores the system to its normal state and then calls its delegate’s [`assessmentSessionDidEnd(_:)`](./assessmentsessiondidend%28_%29.md) method. Confirm to the user that the assessment has stopped only after receiving this callback.

## Parameters

- `session`: The session that ended.

## See Also

### Responding to session start and stop
- [func assessmentSessionDidBegin(AEAssessmentSession)](./assessmentsessiondidbegin%28_%29.md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](./assessmentsession%28_,failedtobeginwitherror%29.md)
  Tells the delegate that the session failed to start.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](./assessmentsession%28_,wasinterruptedwitherror%29.md)
  Tells the delegate that a system failure interrupted the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsessiondidend(_:))*