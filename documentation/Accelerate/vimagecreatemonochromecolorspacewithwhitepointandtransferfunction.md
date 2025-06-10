# vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a monochrome color space based on primitives from Y’CbCr specifications.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(_ whitePoint: UnsafePointer<vImageWhitePoint>, _ tf: UnsafePointer<vImageTransferFunction>, _ intent: CGColorRenderingIntent, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!
```

#### Return Value

A [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) with a reference count of one.

#### Discussion

Use this function to create a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) instance to correspond with a specified white point and a transfer function. The [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) instance defines a monochrome color space. (A Y’CbCr color space is an RGB color space and a conversion matrix from RGB to Y’CbCr.) The white point provides the extent of a color space in XYZ space, and the transfer function provides the transformation from linear color to nonlinear color that the pixels reside in.

## Parameters

- `whitePoint`: Values that define the white point.
- `tf`: The transfer function.
- `intent`: A rendering intent constant that specifies how to handle colors that aren’t within the gamut of the destination color space.
- `flags`: The options to use when performing the operation. This function supports only  , which prints diagnostic information to the console in the event of a failure.
- `error`: A pointer to a  . The function overwrites the pointer to indicate the success or failure of the operation.

## See Also

- [func vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(UnsafePointer<vImageRGBPrimaries>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](vimagecreatergbcolorspacewithprimariesandtransferfunction(_:_:_:_:_:).md)
  Creates an RGB color space based on primitives from Y’CbCr specifications.
- [struct vImageRGBPrimaries](vimagergbprimaries.md)
  A representation of the chromaticity of primaries that define a color space.
- [struct vImageTransferFunction](vimagetransferfunction.md)
  A transfer function to convert from linear to nonlinear RGB.
- [struct vImageWhitePoint](vimagewhitepoint.md)
  A representation of a white point according to the CIE 1931 color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecreatemonochromecolorspacewithwhitepointandtransferfunction(_:_:_:_:_:))*