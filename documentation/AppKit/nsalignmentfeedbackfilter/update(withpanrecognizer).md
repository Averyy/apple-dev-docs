# update(withPanRecognizer:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the feedback filter about a new pan (drag) gesture recognizer event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func update(withPanRecognizer panRecognizer: NSPanGestureRecognizer)
```

```objc
- (void) updateWithPanRecognizer:(NSPanGestureRecognizer *) panRecognizer;
```

## Discussion

This method informs the feedback filter about a new pan (drag) gesture recognizer event. Call this method instead of [`update(with:)`](./update%28with%29.md) if your event tracking uses gesture recognizers.

## Parameters

- `panRecognizer`: The gesture recognizer ([`NSPanGestureRecognizer`](../nspangesturerecognizer.md)) that produced the event.

## See Also

### Related Documentation
- [class NSGestureRecognizer](../nsgesturerecognizer.md)
  An object that monitors events and calls its action method when a predefined sequence of events occur.
- [class NSPanGestureRecognizer](../nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
### Informing the Filter About Events
- [func update(with: NSEvent)](./update%28with%29.md)
  Informs the feedback filter about a new event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/update(withpanrecognizer:))*