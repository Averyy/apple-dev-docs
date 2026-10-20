# colorSpace

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The working color space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var colorSpace: CGColorSpace? { get set }
```

```objc
@property (nonatomic, nullable) CGColorSpaceRef colorSpace;
```

## See Also

### Instance Properties
- [var cubeData: Data](./cubedata.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](./cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](./extrapolate.md)
  If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcubewithcolorspace/colorspace)*