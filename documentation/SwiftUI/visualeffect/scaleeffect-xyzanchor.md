# scaleEffect(x:y:z:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Scales this view by the specified horizontal, vertical, and depth factors.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, z: CGFloat = 1.0, anchor: UnitPoint3D = .center) -> some VisualEffect
```

#### Return Value

An effect that scales this view by `x`,`y`, and `z`.

#### Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `x`: The horizontal scale factor for this view.
- `y`: The vertical scale factor for this view.
- `z`: The depth scale factor for this view.
- `anchor`: The anchor point about which to scale the view. Defaults to center.

## See Also

- [func scaleEffect(_:anchor:)](visualeffect/scaleeffect(_:anchor:).md)
  Scales this view uniformly by the specified factor.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some VisualEffect](visualeffect/scaleeffect(x:y:anchor:).md)
  Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(x:y:z:anchor:))*