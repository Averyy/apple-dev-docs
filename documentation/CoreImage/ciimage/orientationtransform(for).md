# orientationTransform(for:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

The affine transform for changing the image to the given orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func orientationTransform(for orientation: CGImagePropertyOrientation) -> CGAffineTransform
```

```objc
- (CGAffineTransform) imageTransformForCGOrientation:(CGImagePropertyOrientation) orientation;
```

#### Discussion

Returns a [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) for the [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md) value to apply to the image.

## See Also

### Working with Orientation
- [func oriented(CGImagePropertyOrientation) -> CIImage](./oriented%28_%29.md)
  Transforms the original image by a given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/orientationtransform(for:))*