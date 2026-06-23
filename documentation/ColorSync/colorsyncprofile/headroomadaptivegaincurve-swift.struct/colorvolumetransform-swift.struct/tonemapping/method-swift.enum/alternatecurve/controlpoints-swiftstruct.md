# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints

**Framework**: ColorSync  
**Kind**: struct

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
### Instance Properties
- [var slopes: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.property.md)
- [var x: [Float]](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/x.md)
  Input levels normalised to [0, 1]: 0 = reference white, 1 = peak signal.
- [var y: [Float]](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/y.md)
  Gain offsets in stops: positive expands dynamic range, negative compresses it. x.count == y.count (max 32 points).
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.enum.md)
  How slopes at spline control points are determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct)*