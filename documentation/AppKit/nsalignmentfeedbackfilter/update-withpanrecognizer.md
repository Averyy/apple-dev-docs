# update(withPanRecognizer:)

**Framework**: AppKit  
**Kind**: method

Informs the feedback filter about a new pan (drag) gesture recognizer event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func update(withPanRecognizer panRecognizer: NSPanGestureRecognizer)
```

#### Discussion

This method informs the feedback filter about a new pan (drag) gesture recognizer event. Call this method instead of [`update(with:)`](nsalignmentfeedbackfilter/update(with:).md) if your event tracking uses gesture recognizers.

## Parameters

- `panRecognizer`: The gesture recognizer ( ) that produced the event.

## See Also

- [class NSGestureRecognizer](nsgesturerecognizer.md)
  An object that monitors events and calls its action method when a predefined sequence of events occur.
- [class NSPanGestureRecognizer](nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [func update(with: NSEvent)](nsalignmentfeedbackfilter/update(with:).md)
  Informs the feedback filter about a new event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/update(withpanrecognizer:))*