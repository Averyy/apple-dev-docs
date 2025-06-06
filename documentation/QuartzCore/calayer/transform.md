# transform

**Framework**: Core Animation  
**Kind**: property

The transform applied to the layer’s contents. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transform: CATransform3D { get set }
```

#### Discussion

This property is set to the identity transform by default. Any transformations you apply to the layer occur relative to the layer’s anchor point.

## See Also

- [var sublayerTransform: CATransform3D](calayer/sublayertransform.md)
  Specifies the transform to apply to sublayers when rendering. Animatable.
- [func affineTransform() -> CGAffineTransform](calayer/affinetransform.md)
  Returns an affine version of the layer’s transform.
- [func setAffineTransform(CGAffineTransform)](calayer/setaffinetransform(_:).md)
  Sets the layer’s transform to the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/transform)*