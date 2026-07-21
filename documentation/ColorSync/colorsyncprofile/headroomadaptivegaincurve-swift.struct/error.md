# ColorSyncProfile.HeadroomAdaptiveGainCurve.Error

**Framework**: ColorSync  
**Kind**: enum

An error thrown while constructing Headroom Adaptive Gain Curve metadata.

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
enum Error
```

## Topics

### Enumeration Cases
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidCustomChromaticities](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/invalidcustomchromaticities.md)
  The custom chromaticities fall outside the valid range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidHDRReferenceWhite(_:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/invalidhdrreferencewhite(_:).md)
  The custom HDR reference white luminance isn’t greater than `0`.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.mismatchedControlPointArrays(x:y:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/mismatchedcontrolpointarrays(x:y:).md)
  The control points’ `x` and `y` arrays have different counts.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.mismatchedTangentCount(got:expected:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/mismatchedtangentcount(got:expected:).md)
  The number of explicit tangent slopes doesn’t match the control point count.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.negativeBaselineHeadroom(_:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/negativebaselineheadroom(_:).md)
  The baseline headroom is negative.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.negativeHeadroomStops(_:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/negativeheadroomstops(_:).md)
  An alternate curve’s headroom is negative.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.tooManyAlternateCurves(count:limit:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/toomanyalternatecurves(count:limit:).md)
  The number of alternate curves exceeds the limit.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.tooManyControlPoints(count:limit:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/toomanycontrolpoints(count:limit:).md)
  The number of control points exceeds the limit.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.unsupportedApplicationVersion(_:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/unsupportedapplicationversion(_:).md)
  The application version isn’t supported. Only `0` is valid.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.zeroFreeStyleWeights](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/zerofreestyleweights.md)
  A free-style component mix has all-zero weights.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ColorSyncProfile.HeadroomAdaptiveGainCurve](colorsyncprofile/headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/error)*