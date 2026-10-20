# update(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the feedback filter about a new event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func update(with event: NSEvent)
```

```objc
- (void) updateWithEvent:(NSEvent *) event;
```

#### Discussion

This method informs the feedback filter about a new event to be filtered, which matches an event type returned by the [`inputEventMask`](./inputeventmask.md) method. Call the `updateWithEvent:` method instead of [`update(withPanRecognizer:)`](./update%28withpanrecognizer%29.md) if you are using a tracking loop controller for event tracking.

## Parameters

- `event`: An event ([`NSEvent`](../nsevent.md)) to be filtered, which matches an event type returned by the [`inputEventMask`](./inputeventmask.md) method.

## See Also

### Related Documentation
- [class var inputEventMask: NSEvent.EventTypeMask](./inputeventmask.md)
  Retrieves the event types the filter accepts.
### Informing the Filter About Events
- [func update(withPanRecognizer: NSPanGestureRecognizer)](./update%28withpanrecognizer%29.md)
  Informs the feedback filter about a new pan (drag) gesture recognizer event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/update(with:))*