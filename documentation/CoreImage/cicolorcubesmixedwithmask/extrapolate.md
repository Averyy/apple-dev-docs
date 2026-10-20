# extrapolate

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var extrapolate: Bool { get set }
```

```objc
@property (nonatomic) bool extrapolate;
```

## See Also

### Instance Properties
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The working color space.
- [var cube0Data: Data](./cube0data.md)
  The cube texture data to use as a color lookup table.
- [var cube1Data: Data](./cube1data.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](./cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var maskImage: CIImage?](./maskimage.md)
  A masking image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask/extrapolate)*