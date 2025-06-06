# AEAssessmentSessionDelegate

**Framework**: Automatic Assessment Configuration  
**Kind**: protocol

An interface that the session uses to provide information about session state changes to a delegate.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
protocol AEAssessmentSessionDelegate : NSObjectProtocol
```

#### Overview

An assessment session operates asynchronously because it takes time to make the changes associated with starting or stopping a session, and external events might affect the state of the session. Adopt the [`AEAssessmentSessionDelegate`](aeassessmentsessiondelegate.md) protocol to receive callbacks at key points in the session life cycle. Store your adopter in the session’s [`delegate`](aeassessmentsession/delegate.md) property before starting a session.

By listening for delegate callbacks, you learn when you can safely start an assessment after calling the session’s [`begin()`](aeassessmentsession/begin().md) method, when the session has finished after calling the [`end()`](aeassessmentsession/end().md) method, or if the session has been interrupted for some reason. You also find out when it’s safe to proceed after changing a session’s configuration.

The session calls all delegate methods on the main thread.

## Topics

### Responding to session start and stop
- [func assessmentSessionDidBegin(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md)
  Tells the delegate that the session started.
- [func assessmentSession(AEAssessmentSession, failedToBeginWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:failedtobeginwitherror:).md)
  Tells the delegate that the session failed to start.
- [func assessmentSession(AEAssessmentSession, wasInterruptedWithError: any Error)](aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:).md)
  Tells the delegate that a system failure interrupted the session.
- [func assessmentSessionDidEnd(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md)
  Tells the delegate that the session ended.
### Responding to configuration changes
- [func assessmentSessionDidUpdate(AEAssessmentSession)](aeassessmentsessiondelegate/assessmentsessiondidupdate(_:).md)
  Tells the delegate that a configuration update succeeded.
- [func assessmentSession(AEAssessmentSession, failedToUpdateTo: AEAssessmentConfiguration, error: any Error)](aeassessmentsessiondelegate/assessmentsession(_:failedtoupdateto:error:).md)
  Tells the delegate that a configuration update failed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AEAssessmentSessionDelegate)?](aeassessmentsession/delegate.md)
  A delegate to which the session provides state change updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate)*