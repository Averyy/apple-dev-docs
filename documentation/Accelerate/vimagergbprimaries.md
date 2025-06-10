# vImageRGBPrimaries

**Framework**: Accelerate  
**Kind**: struct

A representation of the chromaticity of primaries that define a color space.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImageRGBPrimaries
```

#### Overview

The `x` and `y` values define the chromaticity of each color primary RGB and the white point according to the CIE 1931 color space. For example, the following code defines the RGB primaries for ITU-R BT.709-5:

```swift
var rgbPrimaries = vImageRGBPrimaries(
    red_x: 0.64,
    green_x: 0.3,
    blue_x: 0.15,
    white_x: 0.3127,
    red_y: 0.33,
    green_y: 0.6,
    blue_y: 0.06,
    white_y: 0.329)
```

## Topics

### Initializers
- [init(red_x: Float, green_x: Float, blue_x: Float, white_x: Float, red_y: Float, green_y: Float, blue_y: Float, white_y: Float)](vimagergbprimaries/init(red_x:green_x:blue_x:white_x:red_y:green_y:blue_y:white_y:).md)
  Creates a structure that represents the specified chromaticity of primaries defining a color space.
- [init()](vimagergbprimaries/init.md)
  Creates an empty RGB primaries structure.
### Color primary properties
- [var red_x: Float](vimagergbprimaries/red_x.md)
  The red `x` value according to the CIE 1931 color space.
- [var green_x: Float](vimagergbprimaries/green_x.md)
  The green `x` value according to the CIE 1931 color space.
- [var blue_x: Float](vimagergbprimaries/blue_x.md)
  The blue `x` value according to the CIE 1931 color space.
- [var white_x: Float](vimagergbprimaries/white_x.md)
  The white point `x` value according to the CIE 1931 color space.
- [var red_y: Float](vimagergbprimaries/red_y.md)
  The red `y` value according to the CIE 1931 color space.
- [var green_y: Float](vimagergbprimaries/green_y.md)
  The green_ _`y` value according to the CIE 1931 color space.
- [var blue_y: Float](vimagergbprimaries/blue_y.md)
  The blue `y` value according to the CIE 1931 color space.
- [var white_y: Float](vimagergbprimaries/white_y.md)
  The white point `y` value according to the CIE 1931 color space.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(UnsafePointer<vImageRGBPrimaries>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](vimagecreatergbcolorspacewithprimariesandtransferfunction(_:_:_:_:_:).md)
  Creates an RGB color space based on primitives from Y’CbCr specifications.
- [struct vImageTransferFunction](vimagetransferfunction.md)
  A transfer function to convert from linear to nonlinear RGB.
- [func vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(UnsafePointer<vImageWhitePoint>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](vimagecreatemonochromecolorspacewithwhitepointandtransferfunction(_:_:_:_:_:).md)
  Creates a monochrome color space based on primitives from Y’CbCr specifications.
- [struct vImageWhitePoint](vimagewhitepoint.md)
  A representation of a white point according to the CIE 1931 color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagergbprimaries)*