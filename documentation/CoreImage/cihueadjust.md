# CIHueAdjust

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a hue adjust filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIHueAdjust : CIFilterProtocol
```

```objc
@protocol CIHueAdjust <CIFilter>
```

## Topics

### Instance Properties
- [var angle: Float](./cihueadjust/angle.md)
  An angle, in radians, to use to correct the hue of an image.
- [var inputImage: CIImage?](./cihueadjust/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [class func hueAdjust() -> any CIFilter & CIHueAdjust](./cifilter-swift.class/hueadjust%28%29.md)
  Modifies an image’s hue.
### Protocols
- [protocol CIColorAbsoluteDifference](./cicolorabsolutedifference.md)
- [protocol CIColorClamp](./cicolorclamp.md)
  The properties you use to configure a color clamp filter.
- [protocol CIColorControls](./cicolorcontrols.md)
  The properties you use to configure a color controls filter.
- [protocol CIColorMatrix](./cicolormatrix.md)
  The properties you use to configure a color matrix filter.
- [protocol CIColorPolynomial](./cicolorpolynomial.md)
  The properties you use to configure a color polynomial filter.
- [protocol CIColorThreshold](./cicolorthreshold.md)
- [protocol CIColorThresholdOtsu](./cicolorthresholdotsu.md)
- [protocol CIDepthToDisparity](./cidepthtodisparity.md)
  The properties you use to configure a depth-to-disparity filter.
- [protocol CIDisparityToDepth](./cidisparitytodepth.md)
  The properties you use to configure a disparity-to-depth filter.
- [protocol CIExposureAdjust](./ciexposureadjust.md)
  The properties you use to configure an exposure adjust filter.
- [protocol CIGammaAdjust](./cigammaadjust.md)
  The properties you use to configure a gamma adjust filter.
- [protocol CILinearToSRGBToneCurve](./cilineartosrgbtonecurve.md)
  The properties you use to configure a linear-to-sRGB filter.
- [protocol CISRGBToneCurveToLinear](./cisrgbtonecurvetolinear.md)
  The properties you use to configure an sRGB-to-linear filter.
- [protocol CISystemToneMap](./cisystemtonemap.md)
  The protocol for the System Tone Map filter.
- [protocol CITemperatureAndTint](./citemperatureandtint.md)
  The properties you use to configure a temperature and tint filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihueadjust)*