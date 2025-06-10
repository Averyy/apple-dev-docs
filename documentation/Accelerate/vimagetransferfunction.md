# vImageTransferFunction

**Framework**: Accelerate  
**Kind**: struct

A transfer function to convert from linear to nonlinear RGB.

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
struct vImageTransferFunction
```

#### Overview

The transfer function here is in the style of ITU-R BT.709, and is the inverse operation of what appears in an ICC color profile. For example, the following code defines the transfer function for ITU-R BT.709-5:

```swift
var transferFunction = vImageTransferFunction(
    c0: 1.099,
    c1: 1.0,
    c2: 0.0,
    c3: -0.099,
    gamma: 0.45,
    cutoff: 0.018,
    c4: 4.5,
    c5: 0)
```

The following is the conversion:

```c
if (R >= cutoff) {
    R' = c0 * pow( c1 * R + c2, gamma ) + c3
} 
else {
    R' = c4 * R + c5                             
}
```

## Topics

### Initializers
- [init(c0: CGFloat, c1: CGFloat, c2: CGFloat, c3: CGFloat, gamma: CGFloat, cutoff: CGFloat, c4: CGFloat, c5: CGFloat)](vimagetransferfunction/init(c0:c1:c2:c3:gamma:cutoff:c4:c5:).md)
  Creates a structure that represents a transfer function to convert from linear to nonlinear RGB.
- [init()](vimagetransferfunction/init.md)
  Creates an empty transfer function structure.
### Transfer function properties
- [var c0: CGFloat](vimagetransferfunction/c0.md)
  The `c0` in the transfer function.
- [var c1: CGFloat](vimagetransferfunction/c1.md)
  The `c1` in the transfer function.
- [var c2: CGFloat](vimagetransferfunction/c2.md)
  The `c2` in the transfer function.
- [var c3: CGFloat](vimagetransferfunction/c3.md)
  The `c3` in the transfer function.
- [var cutoff: CGFloat](vimagetransferfunction/cutoff.md)
  The `cutoff` in the transfer function.
- [var gamma: CGFloat](vimagetransferfunction/gamma.md)
  The `gamma` in the transfer function.
- [var c4: CGFloat](vimagetransferfunction/c4.md)
  The `c4` in the transfer function.
- [var c5: CGFloat](vimagetransferfunction/c5.md)
  The `c5` in the transfer function.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(UnsafePointer<vImageRGBPrimaries>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](vimagecreatergbcolorspacewithprimariesandtransferfunction(_:_:_:_:_:).md)
  Creates an RGB color space based on primitives from Y’CbCr specifications.
- [struct vImageRGBPrimaries](vimagergbprimaries.md)
  A representation of the chromaticity of primaries that define a color space.
- [func vImageCreateMonochromeColorSpaceWithWhitePointAndTransferFunction(UnsafePointer<vImageWhitePoint>, UnsafePointer<vImageTransferFunction>, CGColorRenderingIntent, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGColorSpace>!](vimagecreatemonochromecolorspacewithwhitepointandtransferfunction(_:_:_:_:_:).md)
  Creates a monochrome color space based on primitives from Y’CbCr specifications.
- [struct vImageWhitePoint](vimagewhitepoint.md)
  A representation of a white point according to the CIE 1931 color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagetransferfunction)*