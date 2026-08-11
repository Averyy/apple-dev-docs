# kColorSyncComponentMix

**Framework**: ColorSync  
**Kind**: var

Component mixing type (uint8_t) matching `component_mixing_value` in ST 2094-50.

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
var kColorSyncComponentMix: Unmanaged<CFString>
```

#### Discussion

Determines how the framework derives the scalar driving signal from the RGB pixel:

- 0 = MAX(R, G, B)
- 1 = single component (the framework applies the gain curve to individual components)
- 2 = luma_A (sum of 1/6 of each color channel and 1/2 of MAX(R, G, B))
- 3 = free-style (custom linear combination via [`kColorSyncComponentCoefficients`](kcolorsynccomponentcoefficients.md))

Shared across all alternates from index 0 when [`kColorSyncCommonComponentMixing`](kcolorsynccommoncomponentmixing.md) is true.

## See Also

- [var kColorSyncAlternateCurveHeadroomStops: Unmanaged<CFString>](kcolorsyncalternatecurveheadroomstops.md)
  Target headroom of this alternate curve in stops (log2) above reference white (float in the range [0.0, 6.0]). The renderer selects the closest alternate to the actual display headroom.
- [var kColorSyncCommonComponentMixing: Unmanaged<CFString>](kcolorsynccommoncomponentmixing.md)
  CFBooleanRef indicating whether alternate curves share one component-mixing configuration.
- [var kColorSyncCommonCurveParameters: Unmanaged<CFString>](kcolorsynccommoncurveparameters.md)
  CFBooleanRef indicating whether alternate curves share common gain-curve parameters.
- [var kColorSyncControlPointSlopes: Unmanaged<CFString>](kcolorsynccontrolpointslopes.md)
  CFArrayRef of floats — explicit tangent slopes at each control point, expressed as tan(slope_angle). Only present when [`kColorSyncInterpolateSlopes`](kcolorsyncinterpolateslopes.md) is false.
- [var kColorSyncControlPointsX: Unmanaged<CFString>](kcolorsynccontrolpointsx.md)
  CFArrayRef of floats — the X-axis coordinates of the gain-curve control points.
- [var kColorSyncControlPointsY: Unmanaged<CFString>](kcolorsynccontrolpointsy.md)
  CFArrayRef of floats — the Y-axis gain offsets at the control points.
- [var kColorSyncGainCurveChromaticities: Unmanaged<CFString>](kcolorsyncgaincurvechromaticities.md)
  Chromaticity primaries used to compute the driving signal for the gain curve.
- [var kColorSyncInterpolateSlopes: Unmanaged<CFString>](kcolorsyncinterpolateslopes.md)
  CFBooleanRef controlling how the framework determines control-point slopes.
- [var kColorSyncMaxControlPointIndex: Unmanaged<CFString>](kcolorsyncmaxcontrolpointindex.md)
  Index of the last control point (uint8_t, 0–31), i.e. the number of control points minus 1. Shared across all alternates from index 0 when [`kColorSyncCommonCurveParameters`](kcolorsynccommoncurveparameters.md) is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynccomponentmix)*