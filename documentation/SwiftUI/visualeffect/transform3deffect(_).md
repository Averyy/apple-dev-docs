# transform3DEffect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies a 3D transformation to this view’s rendered output.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
func transform3DEffect(_ transform: AffineTransform3D) -> some VisualEffect
```

#### Return Value

An effect that renders transformed according to the provided `transform`

##### Apply a transform about an anchor

This does not adjust the transform relative to an anchor point. Instead, apply the scale and rotation separately using [`scaleEffect(_:anchor:)`](../view/scaleeffect%28_,anchor%29.md) together with [`rotation3DEffect(_:anchor:)`](../view/rotation3deffect%28_,anchor%29.md).

```swift
Model3D(url: URL(string: "https://example.com/robot.usdz")!)
   .scaleEffect(transform.scale)
   .rotation3DEffect(transform.rotation ?? .identity)
   .transform3DEffect(AffineTransform3D(
       translation: transform.translation))
```

## Parameters

- `transform`: The 3D transformation to apply to the view, interpreting it as a 3D plane in space.

## See Also

### Applying a transform
- [func transformEffect(_:)](./transformeffect%28_%29.md)
  Applies an affine transformation to the view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/transform3deffect(_:))*