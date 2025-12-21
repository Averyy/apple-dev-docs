# touchesEnded(_:with:)

**Framework**: RealityKit  
**Kind**: method

Tells the view when one or more fingers are raised from the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?)
```

#### Discussion

See [`touchesEnded(_:with:)`](entitytranslationgesturerecognizer/touchesended(_:with:).md) for more information.

## Parameters

- `touches`: A set of    instances that represent the touches whose values changed. These touches   all belong to the specified  . For touches in a view, this set   contains only one touch by default. To receive multiple touches, set the   view’s     property to  .
- `event`: The event to which the touches belong.

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent?)](arview/touchesbegan(_:with:).md)
  Tells the view that one or more new touches occurred.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](arview/touchesmoved(_:with:).md)
  Tells the view when one or more touches associated with an event changed.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](arview/touchescancelled(_:with:).md)
  Tells the view when a system event (such as a system alert) cancels a touch sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/touchesended(_:with:))*