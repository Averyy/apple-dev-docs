# exposureAdaptationDarkeningSpeedFactor

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The relative duration of automatically animated exposure transitions from bright to dark areas.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var exposureAdaptationDarkeningSpeedFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat exposureAdaptationDarkeningSpeedFactor;
```

#### Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called *tone mapping* to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. When the [`wantsExposureAdaptation`](./wantsexposureadaptation.md) property is enabled, SceneKit automatically adjusts the tone mapping curve based on the average luminance currently visible to the camera, and creates automatic transitions between exposure levels.

SceneKit automatically determines the overall duration of exposure-level animations based on the values of this property and the [`exposureAdaptationDarkeningSpeedFactor`](./exposureadaptationdarkeningspeedfactor.md) property. The default value is `0.6`, resulting in darkening animations that are slightly faster than brighting animations.

This property has no effect if either of the [`wantsHDR`](./wantshdr.md) or [`wantsExposureAdaptation`](./wantsexposureadaptation.md) values is [`false`](../../Swift/false.md).

## See Also

### Adding Automatic HDR Exposure Adaptation
- [var wantsExposureAdaptation: Bool](./wantsexposureadaptation.md)
  A Boolean value that determines whether SceneKit automatically adjusts the exposure level.
- [var exposureAdaptationBrighteningSpeedFactor: CGFloat](./exposureadaptationbrighteningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from dark to bright areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/exposureadaptationdarkeningspeedfactor)*