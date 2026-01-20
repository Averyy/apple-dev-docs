# CIGammaAdjust

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a gamma adjust filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIGammaAdjust : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cigammaadjust/inputimage.md)
  The image to use as an input image.
- [var power: Float](cigammaadjust/power.md)
  A gamma value to use to correct image brightness.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](cifilter-swift.class/gammaadjust.md)
  Alters an image’s transition between black and white.
- [protocol CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [protocol CIColorClamp](cicolorclamp.md)
  The properties you use to configure a color clamp filter.
- [protocol CIColorControls](cicolorcontrols.md)
  The properties you use to configure a color controls filter.
- [protocol CIColorMatrix](cicolormatrix.md)
  The properties you use to configure a color matrix filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigammaadjust)*