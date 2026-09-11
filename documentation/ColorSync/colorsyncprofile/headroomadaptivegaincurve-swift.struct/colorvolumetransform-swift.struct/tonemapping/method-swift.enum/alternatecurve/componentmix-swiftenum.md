# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix

**Framework**: ColorSync  
**Kind**: enum

How the framework derives the scalar driving signal for a gain curve from an RGB pixel.

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
enum ComponentMix
```

## Topics

### Enumeration Cases
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix.freeStyle(red:green:blue:maxRGB:minRGB:component:)](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum/freestyle(red:green:blue:maxrgb:minrgb:component:).md)
  signal = R·`red` + G·`green` + B·`blue` + MAX(R,G,B)·`maxRGB` + MIN(R,G,B)·`minRGB` + C·`component`
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix.lumaA](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum/lumaa.md)
  Equal-weighted luminance (sum of 1/6 of each color channel + 1/2 of MAX(R, G, B)).
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix.maxRGB](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum/maxrgb.md)
  Use the maximum of the red, green, and blue components.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix.perComponent](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum/percomponent.md)
  Apply the curve independently to each channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum)*