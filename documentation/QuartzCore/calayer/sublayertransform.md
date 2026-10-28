# sublayerTransform

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Specifies the transform to apply to sublayers when rendering. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sublayerTransform: CATransform3D { get set }
```

```objc
@property CATransform3D sublayerTransform;
```

## Discussion

You typically use this property to add perspective and other viewing effects to embedded layers. You add perspective by setting the sublayer transform to the desired projection matrix. The default value of this property is the identity transform.

## See Also

### Managing the layer’s transform
- [var transform: CATransform3D](./transform.md)
  The transform applied to the layer’s contents. Animatable.
- [func affineTransform() -> CGAffineTransform](./affinetransform%28%29.md)
  Returns an affine version of the layer’s transform.
- [func setAffineTransform(CGAffineTransform)](./setaffinetransform%28_%29.md)
  Sets the layer’s transform to the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/sublayertransform)*