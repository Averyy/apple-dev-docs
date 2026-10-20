# inputImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * inputImage;
```

## See Also

### Instance Properties
- [var decay: Float](./decay.md)
  A value that determines how fast the color fades from the center triangle.
- [var point: CGPoint](./point.md)
  The x and y position to use as the center of the triangular area in the input image.
- [var rotation: Float](./rotation.md)
  The rotation angle of the triangle.
- [var size: Float](./size.md)
  The size, in pixels, of the triangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citrianglekaleidoscope/inputimage)*