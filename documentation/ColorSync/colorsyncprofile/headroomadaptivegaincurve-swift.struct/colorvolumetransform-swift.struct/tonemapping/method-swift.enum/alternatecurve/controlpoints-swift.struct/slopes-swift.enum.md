# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes

**Framework**: ColorSync  
**Kind**: enum  
**Role**: Enumeration

How the framework determines slopes at spline control points.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Slopes
```

## Topics

### Enumeration Cases
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes.interpolate](./slopes-swift.enum/interpolate.md)
  The framework computes slopes by Piecewise Cubic Hermite Interpolating Polynomial from the X/Y coordinates.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes.tangent(_:)](./slopes-swift.enum/tangent%28_%29.md)
  Explicit tangent slopes expressed as tan(slope_angle), one per control point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.enum)*