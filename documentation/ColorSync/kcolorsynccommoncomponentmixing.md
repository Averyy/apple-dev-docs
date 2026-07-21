# kColorSyncCommonComponentMixing

**Framework**: ColorSync  
**Kind**: var

CFBooleanRef. When true, all alternate curves share the component mixing configuration from array index 0, reducing bitstream size.

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
var kColorSyncCommonComponentMixing: Unmanaged<CFString>
```

## See Also

- [var kColorSyncAlternateCurveHeadroomStops: Unmanaged<CFString>](kcolorsyncalternatecurveheadroomstops.md)
  Target headroom of this alternate curve in stops (log2) above reference white (float in the range [0.0, 6.0]). The renderer selects the closest alternate to the actual display headroom.
- [var kColorSyncCommonCurveParameters: Unmanaged<CFString>](kcolorsynccommoncurveparameters.md)
  CFBooleanRef. When true, all alternate curves share the gain curve x control points, and slope interpolate flag from array index 0, reducing bitstream size.
- [var kColorSyncComponentMix: Unmanaged<CFString>](kcolorsynccomponentmix.md)
  Component mixing type (uint8_t) matching `component_mixing_value` in ST 2094-50.
- [var kColorSyncControlPointSlopes: Unmanaged<CFString>](kcolorsynccontrolpointslopes.md)
  CFArrayRef of floats — explicit tangent slopes at each control point, expressed as tan(slope_angle). Only present when `kColorSyncInterpolateSlopes` is false.
- [var kColorSyncControlPointsX: Unmanaged<CFString>](kcolorsynccontrolpointsx.md)
  CFArrayRef of floating-point values representing the X-axis coordinates of the gain-curve control points, normalized by the reference white, thus a value of 1.0 corresponds to the signal value at reference white. Shared across all alternates from index 0 when `kColorSyncCommonCurveParameters` is true.
- [var kColorSyncControlPointsY: Unmanaged<CFString>](kcolorsynccontrolpointsy.md)
  CFArrayRef of floats — Y-axis gain offsets at the control points, in stops (float in the range [0.0, 6.0]). Values must be non-negative; the gain direction (expand vs. compress) is inferred from the relationship between this alternate’s headroom and the baseline headroom.
- [var kColorSyncGainCurveChromaticities: Unmanaged<CFString>](kcolorsyncgaincurvechromaticities.md)
  Chromaticity primaries used to compute the driving signal for the gain curve.
- [var kColorSyncInterpolateSlopes: Unmanaged<CFString>](kcolorsyncinterpolateslopes.md)
  CFBooleanRef. When true, slopes at control points are computed by Piecewise Cubic Hermite Interpolating Polynomial from the X,Y control point coordinates, and `kColorSyncControlPointSlopes` must be absent. When false, explicit slopes must be supplied in `kColorSyncControlPointSlopes` (see below). Shared across all alternates from index 0 when `kColorSyncCommonCurveParameters` is true.
- [var kColorSyncMaxControlPointIndex: Unmanaged<CFString>](kcolorsyncmaxcontrolpointindex.md)
  Index of the last control point (uint8_t, 0–31), i.e. the number of control points minus 1. Shared across all alternates from index 0 when `kColorSyncCommonCurveParameters` is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynccommoncomponentmixing)*