# cancel()

**Framework**: UIKit  
**Kind**: method

Cancels the current preview interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cancel()
```

#### Discussion

When a preview interaction is in progress, use this method to cancel it, preventing any further callbacks to the delegate methods.

## See Also

- [var view: UIView?](uipreviewinteraction/view.md)
  The view from which the preview interaction receives touch events.
- [func location(in: (any UICoordinateSpace)?) -> CGPoint](uipreviewinteraction/location(in:).md)
  Returns the location of the touch that started the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteraction/cancel())*