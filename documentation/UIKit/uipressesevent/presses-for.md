# presses(for:)

**Framework**: UIKit  
**Kind**: method

Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presses(for gesture: UIGestureRecognizer) -> Set<UIPress>
```

#### Return Value

The set of [`UIPress`](uipress.md) instances that participated in this event that are associated with the gesture recognizer.

## Parameters

- `gesture`: A gesture recognizer.

## See Also

- [var allPresses: Set<UIPress>](uipressesevent/allpresses.md)
  The state of all physical buttons in the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipressesevent/presses(for:))*