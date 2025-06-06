# touchesCancelled(_:with:)

**Framework**: RealityKit  
**Kind**: method

Tells the view when a system event (such as a system alert) cancels a touch sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?)
```

#### Discussion

See [`touchesCancelled(_:with:)`](https://developer.apple.com/documentation/UIKit/UIResponder/touchesCancelled(_:with:)) for more information.

## Parameters

- `touches`: A set of    instances that represent the touches whose values changed. These touches   all belong to the specified  . For touches in a view, this set   contains only one touch by default. To receive multiple touches, set the   view’s     property to  .
- `event`: The event to which the touches belong.

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent?)](arview/touchesbegan(_:with:).md)
  Tells the view that one or more new touches occurred.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](arview/touchesmoved(_:with:).md)
  Tells the view when one or more touches associated with an event changed.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](arview/touchesended(_:with:).md)
  Tells the view when one or more fingers are raised from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/touchescancelled(_:with:))*