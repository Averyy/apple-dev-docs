# assessmentSession(_:wasInterruptedWithError:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) assessmentSession:(AEAssessmentSession *) session wasInterruptedWithError:(NSError *) error;
```

#### Discussion

If one or more subsystems fail during a session, the session tells its delegate by calling the [`assessmentSession(_:wasInterruptedWithError:)`](./assessmentsession%28_,wasinterruptedwitherror%29.md) method. If your app receives this callback, immediately stop the assessment, hide all sensitive content, and end the session. Because it might take time for your app to stop the assessment, the session relies on your app to call the [`end()`](../aeassessmentsession/end%28%29.md) method:

**Swift**:

```swift
func assessmentSession(_ session: AEAssessmentSession, wasInterruptedWithError error: Error) {
    // Hide sensitive UI and optionally store assessment progress.

    // End the session.
    session.end()
}
```

**Objective-C**:

```objc
- (void)assessmentSession:(AEAssessmentSession *)session wasInterruptedWithError:(NSError *)error {
    // Hide sensitive UI and optionally store assessment progress.

    // End the session.
    [session end];
}
```

## Parameters

- `session`: The session that failed.
- `error`: An error that provides information about the interruption.

## See Also

### Responding to session start and stop
- [func assessmentSessionDidBegin(AEAssessmentSession)](./assessmentsessiondidbegin%28_%29.md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](./assessmentsession%28_,failedtobeginwitherror%29.md)
  Tells the delegate that the session failed to start.
- [func assessmentSessionDidEnd(AEAssessmentSession)](./assessmentsessiondidend%28_%29.md)
  Tells the delegate that the session ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:))*