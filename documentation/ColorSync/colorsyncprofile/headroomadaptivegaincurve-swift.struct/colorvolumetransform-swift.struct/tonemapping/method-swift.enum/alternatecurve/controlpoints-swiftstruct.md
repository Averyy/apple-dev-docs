# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints

**Framework**: ColorSync  
**Kind**: struct

The spline control points that define a gain curve.

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
struct ControlPoints
```

## Topics

### Initializers
- [init(x: [Float], y: [Float], slopes: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes) throws](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/init(x:y:slopes:).md)
  Creates a set of spline control points.
### Instance Properties
- [var slopes: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.property.md)
  How the framework determines the slope at each control point.
- [var x: [Float]](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/x.md)
  Input levels normalized by reference white: 1.0 = reference white.
- [var y: [Float]](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/y.md)
  Gain offsets in stops (non-negative): the framework infers direction (expand vs. compress) from the relationship between this alternate’s headroom and the baseline headroom.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.enum.md)
  How the framework determines slopes at spline control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct)*