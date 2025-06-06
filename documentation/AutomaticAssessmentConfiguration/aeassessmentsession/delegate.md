# delegate

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A delegate to which the session provides state change updates.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
weak var delegate: (any AEAssessmentSessionDelegate)? { get set }
```

#### Discussion

An assessment session operates asynchronously because it takes time to make the changes associated with starting or stopping a session, and external events might affect the state of the session. Adopt the [`AEAssessmentSessionDelegate`](aeassessmentsessiondelegate.md) protocol to receive callbacks at key points in the session life cycle. Store your adopter in the session’s [`delegate`](aeassessmentsession/delegate.md) property before starting a session.

By listening for delegate callbacks, you learn when you can safely start an assessment after calling the session’s [`begin()`](aeassessmentsession/begin().md) method, when the session has finished after calling the [`end()`](aeassessmentsession/end().md) method, or if the session has been interrupted for some reason.

The session calls all delegate methods on the main thread.

## See Also

- [protocol AEAssessmentSessionDelegate](aeassessmentsessiondelegate.md)
  An interface that the session uses to provide information about session state changes to a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/delegate)*