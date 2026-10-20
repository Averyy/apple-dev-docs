# touchesBegan(_:with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that one or more new touches occurred.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?)
```

#### Discussion

See [`touchesBegan(_:with:)`](../../UIKit/uiresponder/touchesbegan%28_,with%29.md) for more information.

## Parameters

- `touches`: A set of `UITouch` instances that represent the touches whose values changed. These touches all belong to the specified `event`. For touches in a view, this set contains only one touch by default. To receive multiple touches, set the view’s [`isMultipleTouchEnabled`](../../UIKit/uiview/ismultipletouchenabled.md) property to `true`.
- `event`: The event to which the touches belong.

## See Also

### Handling touch input
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](./touchesmoved%28_,with%29.md)
  Tells the view when one or more touches associated with an event changed.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](./touchesended%28_,with%29.md)
  Tells the view when one or more fingers are raised from the view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](./touchescancelled%28_,with%29.md)
  Tells the view when a system event (such as a system alert) cancels a touch sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/touchesbegan(_:with:))*