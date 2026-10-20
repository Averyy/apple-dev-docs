# oriented(_:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Transforms the original image by a given orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func oriented(_ orientation: CGImagePropertyOrientation) -> CIImage
```

```objc
- (CIImage *) imageByApplyingCGOrientation:(CGImagePropertyOrientation) orientation;
```

#### Discussion

Returns a new image representing the original image transformed for the given [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md).

## See Also

### Working with Orientation
- [func orientationTransform(for: CGImagePropertyOrientation) -> CGAffineTransform](./orientationtransform%28for%29.md)
  The affine transform for changing the image to the given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/oriented(_:))*