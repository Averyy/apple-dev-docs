# affineTransform()

**Framework**: Core Animation  
**Kind**: method

Returns an affine version of the layer’s transform.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func affineTransform() -> CGAffineTransform
```

#### Return Value

The affine transform structure that corresponds to the value in the layer’s [`transform`](calayer/transform.md) property.

## See Also

- [var transform: CATransform3D](calayer/transform.md)
  The transform applied to the layer’s contents. Animatable.
- [var sublayerTransform: CATransform3D](calayer/sublayertransform.md)
  Specifies the transform to apply to sublayers when rendering. Animatable.
- [func setAffineTransform(CGAffineTransform)](calayer/setaffinetransform(_:).md)
  Sets the layer’s transform to the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/affinetransform())*