# view

**Framework**: UIKit  
**Kind**: property

The view from which the preview interaction receives touch events.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var view: UIView? { get }
```

#### Discussion

A preview interaction operates on the view that’s provided at initialization time. Use this property to obtain a reference to that same view. Note that this is a weak property — the preview interaction doesn’t retain a reference to the view it’s provided.

## See Also

- [func cancel()](uipreviewinteraction/cancel.md)
  Cancels the current preview interaction.
- [func location(in: (any UICoordinateSpace)?) -> CGPoint](uipreviewinteraction/location(in:).md)
  Returns the location of the touch that started the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteraction/view)*