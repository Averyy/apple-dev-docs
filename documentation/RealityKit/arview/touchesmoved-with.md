# touchesMoved(_:with:)

**Framework**: RealityKit  
**Kind**: method

Tells the view when one or more touches associated with an event changed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?)
```

#### Discussion

See [`touchesMoved(_:with:)`](https://developer.apple.com/documentation/UIKit/UIResponder/touchesMoved(_:with:)) for more information.

## Parameters

- `touches`: A set of    instances that represent the touches whose values changed. These touches   all belong to the specified  . For touches in a view, this set   contains only one touch by default. To receive multiple touches, set the   view’s     property to  .
- `event`: The event to which the touches belong.

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent?)](arview/touchesbegan(_:with:).md)
  Tells the view that one or more new touches occurred.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](arview/touchesended(_:with:).md)
  Tells the view when one or more fingers are raised from the view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](arview/touchescancelled(_:with:).md)
  Tells the view when a system event (such as a system alert) cancels a touch sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/touchesmoved(_:with:))*