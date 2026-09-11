# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix.freeStyle(red:green:blue:maxRGB:minRGB:component:)

**Framework**: ColorSync  
**Kind**: case

signal = R·`red` + G·`green` + B·`blue` + MAX(R,G,B)·`maxRGB` + MIN(R,G,B)·`minRGB` + C·`component`

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
case freeStyle(red: Float = 0.0, green: Float = 0.0, blue: Float = 0.0, maxRGB: Float = 0.0, minRGB: Float = 0.0, component: Float = 0.0)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/componentmix-swift.enum/freestyle(red:green:blue:maxrgb:minrgb:component:))*