# vImageWhitePoint

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A representation of a white point according to the CIE 1931 color space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct vImageWhitePoint
```

```c
typedef struct vImageWhitePoint { ... } vImageWhitePoint;
```

## Topics

### Initializers
- [init(white_x: Float, white_y: Float)](./vimagewhitepoint/init%28white_x,white_y%29.md)
  Creates a structure that represents a white point according to the CIE 1931 color space.
- [init()](./vimagewhitepoint/init%28%29.md)
  Creates an empty structure that represents a white point.
### White point properties
- [var white_x: Float](./vimagewhitepoint/white_x.md)
  The white point `x` value according to the CIE 1931 color space.
- [var white_y: Float](./vimagewhitepoint/white_y.md)
  The white point `y` value according to the CIE 1931 color space.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Creating Core Graphics color spaces
- [func vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(UnsafePointer<vImageRGBPrimaries>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](./vimagecreatergbcolorspacewithprimariesandtransferfunction%28_,_,_,_,_%29.md)
  Creates an RGB color space based on primitives from Y’CbCr specifications.
- [struct vImageRGBPrimaries](./vimagergbprimaries.md)
  A representation of the chromaticity of primaries that define a color space.
- [struct vImageTransferFunction](./vimagetransferfunction.md)
  A transfer function to convert from linear to nonlinear RGB.
- [func vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(UnsafePointer<vImageWhitePoint>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](./vimagecreatemonochromecolorspacewithwhitepointandtransferfunction%28_,_,_,_,_%29.md)
  Creates a monochrome color space based on primitives from Y’CbCr specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagewhitepoint)*