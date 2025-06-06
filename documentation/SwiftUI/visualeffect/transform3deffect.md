# transform3DEffect(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies a 3D transformation to the receiver.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func transform3DEffect(_ transform: AffineTransform3D) -> some VisualEffect
```

#### Return Value

An effect that renders transformed according to the provided `transform`

## Parameters

- `transform`: The 3D transformation to apply to the view,   interpreting it as a 3D plane in space.

## See Also

- [func transformEffect(_:)](visualeffect/transformeffect(_:).md)
  Applies an affine transformation to the view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/transform3deffect(_:))*