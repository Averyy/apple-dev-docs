# exposureAdaptationDarkeningSpeedFactor

**Framework**: SceneKit  
**Kind**: property

The relative duration of automatically animated exposure transitions from bright to dark areas.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var exposureAdaptationDarkeningSpeedFactor: CGFloat { get set }
```

#### Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called  to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. When the [`wantsExposureAdaptation`](scncamera/wantsexposureadaptation.md) property is enabled, SceneKit automatically adjusts the tone mapping curve based on the average luminance currently visible to the camera, and creates automatic transitions between exposure levels.

SceneKit automatically determines the overall duration of exposure-level animations based on the values of this property and the [`exposureAdaptationDarkeningSpeedFactor`](scncamera/exposureadaptationdarkeningspeedfactor.md) property. The default value is `0.6`, resulting in darkening animations that are slightly faster than brighting animations.

This property has no effect if either of the [`wantsHDR`](scncamera/wantshdr.md) or [`wantsExposureAdaptation`](scncamera/wantsexposureadaptation.md) values is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var wantsExposureAdaptation: Bool](scncamera/wantsexposureadaptation.md)
  A Boolean value that determines whether SceneKit automatically adjusts the exposure level.
- [var exposureAdaptationBrighteningSpeedFactor: CGFloat](scncamera/exposureadaptationbrighteningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from dark to bright areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/exposureadaptationdarkeningspeedfactor)*