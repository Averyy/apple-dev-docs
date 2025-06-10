# transform3DEffect(_:)

**Framework**: Assignables  
**Kind**: method

Applies a 3D transformation to this view’s rendered output.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func transform3DEffect(_ transform: AffineTransform3D) -> some View
```

#### Return Value

A view that renders transformed according to the provided `transform`

##### Apply a Transform About an Anchor

This does not adjust the transform relative to an anchor point. Instead, apply the scale and rotation separately using `View/scaleEffect(_:anchor:)` together with `View/rotation3DEffect(_:anchor:)`.

```swift
Model3D(url: URL(string: "https://example.com/robot.usdz")!)
   .scaleEffect(transform.scale)
   .rotation3DEffect(transform.rotation ?? .identity)
   .transform3DEffect(AffineTransform3D(
       translation: transform.translation))
```

## Parameters

- `transform`: The 3D transformation to apply to the view,   interpreting it as a 3D plane in space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/transform3deffect(_:))*