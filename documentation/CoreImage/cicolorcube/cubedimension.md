# cubeDimension

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The length, in texels, of each side of the cube texture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var cubeDimension: Float { get set }
```

## See Also

- [var cubeData: Data](cicolorcube/cubedata.md)
  The cube texture data to use as a color lookup table.
- [var inputImage: CIImage?](cicolorcube/inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](cicolorcube/extrapolate.md)
  If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcube/cubedimension)*