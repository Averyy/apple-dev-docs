# CIToneCurve

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a tone curve filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIToneCurve : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](citonecurve/inputimage.md)
  The image to use as an input image.
- [var point0: CGPoint](citonecurve/point0.md)
  A vector containing the position of the first point of the tone curve.
- [var point1: CGPoint](citonecurve/point1.md)
  A vector containing the position of the second point of the tone curve.
- [var point2: CGPoint](citonecurve/point2.md)
  A vector containing the position of the third point of the tone curve.
- [var point3: CGPoint](citonecurve/point3.md)
  A vector containing the position of the fourth point of the tone curve.
- [var point4: CGPoint](citonecurve/point4.md)
  A vector containing the position of the fifth point of the tone curve.
- [var extrapolate: Bool](citonecurve/extrapolate.md)
  If true, then the color effect will be extrapolated if the input image contains RGB component values outside the range 0.0 to 1.0.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter-swift.class/tonecurve.md)
  Alters an image’s tone curve according to a series of data points.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citonecurve)*