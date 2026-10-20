# setAffineTransform(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Sets the layer’s transform to the specified affine transform.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setAffineTransform(_ m: CGAffineTransform)
```

```objc
- (void) setAffineTransform:(CGAffineTransform) m;
```

## Parameters

- `m`: The affine transform to use for the layer’s transform.

## See Also

### Managing the layer’s transform
- [var transform: CATransform3D](./transform.md)
  The transform applied to the layer’s contents. Animatable.
- [var sublayerTransform: CATransform3D](./sublayertransform.md)
  Specifies the transform to apply to sublayers when rendering. Animatable.
- [func affineTransform() -> CGAffineTransform](./affinetransform%28%29.md)
  Returns an affine version of the layer’s transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/setaffinetransform(_:))*