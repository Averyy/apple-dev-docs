# update(with:)

**Framework**: AppKit  
**Kind**: method

Informs the feedback filter about a new event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func update(with event: NSEvent)
```

#### Discussion

This method informs the feedback filter about a new event to be filtered, which matches an event type returned by the [`inputEventMask`](nsalignmentfeedbackfilter/inputeventmask.md) method. Call the `updateWithEvent:` method instead of [`update(withPanRecognizer:)`](nsalignmentfeedbackfilter/update(withpanrecognizer:).md) if you are using a tracking loop controller for event tracking.

## Parameters

- `event`: An event ( ) to be filtered, which matches an event type returned by the   method.

## See Also

- [class var inputEventMask: NSEvent.EventTypeMask](nsalignmentfeedbackfilter/inputeventmask.md)
  Retrieves the event types the filter accepts.
- [func update(withPanRecognizer: NSPanGestureRecognizer)](nsalignmentfeedbackfilter/update(withpanrecognizer:).md)
  Informs the feedback filter about a new pan (drag) gesture recognizer event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/update(with:))*