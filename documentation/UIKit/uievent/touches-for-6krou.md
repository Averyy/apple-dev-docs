# touches(for:)

**Framework**: UIKit  
**Kind**: method

Returns the touch objects that are being delivered to the specified gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func touches(for gesture: UIGestureRecognizer) -> Set<UITouch>?
```

#### Return Value

A set of [`UITouch`](uitouch.md) objects representing the touches being delivered to the specified gesture recognizer for the event represented by the receiver.

## Parameters

- `gesture`: An instance of a subclass of the abstract base class UIGestureRecognizer. This gesture-recognizer object must be attached to a view to receive the touches hit-tested to that view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/touches(for:)-6krou)*