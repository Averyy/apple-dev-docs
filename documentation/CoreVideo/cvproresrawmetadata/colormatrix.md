# colorMatrix

**Framework**: Core Video  
**Kind**: property

This is a 3x3 matrix which transforms linear RGB pixel values in the camera native color space to CIE 1931 XYZ values relative to the D65 illuminant, where the matrix entries are stored in row-major order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var colorMatrix: InlineArray<9, Float32>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/colormatrix)*