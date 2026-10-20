# transform

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CATransform3D transform;
```

#### Discussion

This property is set to the identity transform by default. Any transformations you apply to the layer occur relative to the layer’s anchor point.

## See Also

### Managing the layer’s transform
- [var sublayerTransform: CATransform3D](./sublayertransform.md)
  Specifies the transform to apply to sublayers when rendering. Animatable.
- [func affineTransform() -> CGAffineTransform](./affinetransform%28%29.md)
  Returns an affine version of the layer’s transform.
- [func setAffineTransform(CGAffineTransform)](./setaffinetransform%28_%29.md)
  Sets the layer’s transform to the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/transform)*