# CIColorMatrix

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a color matrix filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIColorMatrix : CIFilterProtocol
```

## Topics

### Instance Properties
- [var aVector: CIVector](cicolormatrix/avector.md)
  The amount of alpha to multiply the source color values by.
- [var bVector: CIVector](cicolormatrix/bvector.md)
  The amount of blue to multiply the source color values by.
- [var gVector: CIVector](cicolormatrix/gvector.md)
  The amount of green to multiply the source color values by.
- [var rVector: CIVector](cicolormatrix/rvector.md)
  The amount of red to multiply the source color values by.
- [var biasVector: CIVector](cicolormatrix/biasvector.md)
  A vector that’s added to each color component.
- [var inputImage: CIImage?](cicolormatrix/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorMatrix() -> any CIFilter & CIColorMatrix](cifilter-swift.class/colormatrix.md)
  Alters the colors in an image based on vectors provided.
- [protocol CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [protocol CIColorClamp](cicolorclamp.md)
  The properties you use to configure a color clamp filter.
- [protocol CIColorControls](cicolorcontrols.md)
  The properties you use to configure a color controls filter.
- [protocol CIColorPolynomial](cicolorpolynomial.md)
  The properties you use to configure a color polynomial filter.
- [protocol CIColorThreshold](cicolorthreshold.md)
- [protocol CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [protocol CIDepthToDisparity](cidepthtodisparity.md)
  The properties you use to configure a depth-to-disparity filter.
- [protocol CIDisparityToDepth](cidisparitytodepth.md)
  The properties you use to configure a disparity-to-depth filter.
- [protocol CIExposureAdjust](ciexposureadjust.md)
  The properties you use to configure an exposure adjust filter.
- [protocol CIGammaAdjust](cigammaadjust.md)
  The properties you use to configure a gamma adjust filter.
- [protocol CIHueAdjust](cihueadjust.md)
  The properties you use to configure a hue adjust filter.
- [protocol CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md)
  The properties you use to configure a linear-to-sRGB filter.
- [protocol CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md)
  The properties you use to configure an sRGB-to-linear filter.
- [protocol CISystemToneMap](cisystemtonemap.md)
  The protocol for the System Tone Map filter.
- [protocol CITemperatureAndTint](citemperatureandtint.md)
  The properties you use to configure a temperature and tint filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormatrix)*