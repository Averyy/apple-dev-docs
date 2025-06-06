# allPresses

**Framework**: UIKit  
**Kind**: property

The state of all physical buttons in the event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allPresses: Set<UIPress> { get }
```

#### Return Value

The set of [`UIPress`](uipress.md) instances that participated in this event.

## See Also

- [func presses(for: UIGestureRecognizer) -> Set<UIPress>](uipressesevent/presses(for:).md)
  Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipressesevent/allpresses)*