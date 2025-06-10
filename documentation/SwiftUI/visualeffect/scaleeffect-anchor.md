# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Scales this view uniformly by the specified factor, relative to an anchor point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some VisualEffect
```

#### Return Value

An effect that scales this view by `s` in all dimensions.

#### Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `s`: The scale factor for this view.
- `anchor`: The anchor point about which to scale the view. Defaults to center.

## See Also

- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some VisualEffect](visualeffect/scaleeffect(x:y:anchor:).md)
  Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(_:anchor:))*