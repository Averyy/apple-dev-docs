# transformEffect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies an affine transformation to the view’s rendered output.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func transformEffect(_ transform: CGAffineTransform) -> some VisualEffect
```

**Other overloads**:

```swift
func transformEffect(_ transform: ProjectionTransform) -> some VisualEffect
```

## Return Value

An effect that applies an affine transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md).

## Parameters

- `transform`: A [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply to the view.

## See Also

### Applying a transform
- [func transform3DEffect(AffineTransform3D) -> some VisualEffect](./transform3deffect%28_%29.md)
  Applies a 3D transformation to this view’s rendered output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/transformeffect(_:))*