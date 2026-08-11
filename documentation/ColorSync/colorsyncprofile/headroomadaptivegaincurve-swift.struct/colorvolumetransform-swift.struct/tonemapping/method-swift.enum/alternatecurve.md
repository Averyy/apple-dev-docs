# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve

**Framework**: ColorSync  
**Kind**: struct

An alternate gain curve that targets a specific display headroom level.

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
struct AlternateCurve
```

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct.md)
  The spline control points that define a gain curve.
### Initializers
- [init(headroomStops: Float, componentMix: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix, controlPoints: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints) throws](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/init(headroomstops:componentmix:controlpoints:).md)
  Creates an alternate gain curve.
### Instance Properties
- [var componentMix: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.property.md)
  How the framework derives the scalar driving signal from each RGB pixel.
- [var controlPoints: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.property.md)
  Spline control points defining a gain curve.
- [var headroomStops: Float](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/headroomstops.md)
  Alternate headroom in stops above reference white.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum.md)
  How the framework derives the scalar driving signal for a gain curve from an RGB pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve)*