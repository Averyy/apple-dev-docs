# CIColorPolynomial

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a color polynomial filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIColorPolynomial : CIFilterProtocol
```

## Topics

### Instance Properties
- [var alphaCoefficients: CIVector](cicolorpolynomial/alphacoefficients.md)
  Polynomial coefficients for the alpha channel.
- [var blueCoefficients: CIVector](cicolorpolynomial/bluecoefficients.md)
  Polynomial coefficients for the blue channel.
- [var greenCoefficients: CIVector](cicolorpolynomial/greencoefficients.md)
  Polynomial coefficients for the green channel.
- [var inputImage: CIImage?](cicolorpolynomial/inputimage.md)
  The image to use as an input image.
- [var redCoefficients: CIVector](cicolorpolynomial/redcoefficients.md)
  Polynomial coefficients for the red channel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](cifilter-swift.class/colorpolynomial.md)
  Alters an image’s colors.
- [protocol CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [protocol CIColorClamp](cicolorclamp.md)
  The properties you use to configure a color clamp filter.
- [protocol CIColorControls](cicolorcontrols.md)
  The properties you use to configure a color controls filter.
- [protocol CIColorMatrix](cicolormatrix.md)
  The properties you use to configure a color matrix filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorpolynomial)*