# wantsExposureAdaptation

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit automatically adjusts the exposure level.

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
var wantsExposureAdaptation: Bool { get set }
```

#### Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called  to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. One measure of tone mapping is the exposure value, whose effect on the output is similar to that of the shutter speed (or exposure time) of a real-world camera—lower exposure values result in a darker image, and higher exposures result in a brighter image. You cannot adjust exposure value directly—instead, SceneKit determines a tone mapping curve (including the exposure level) from the [`minimumExposure`](scncamera/minimumexposure.md), [`maximumExposure`](scncamera/maximumexposure.md), [`exposureOffset`](scncamera/exposureoffset.md), and [`whitePoint`](scncamera/whitepoint.md) properties along with a measure of scene luminance.

If this property’s value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), SceneKit automatically measures the current luminance visible to the camera during rendering, and adjusts the exposure level accordingly. Additionally, when the scene luminance changes, SceneKit automatically animates a transition to the new exposure level (see the [`exposureAdaptationBrighteningSpeedFactor`](scncamera/exposureadaptationbrighteningspeedfactor.md) and [`exposureAdaptationDarkeningSpeedFactor`](scncamera/exposureadaptationdarkeningspeedfactor.md) properties).

> **Note**:  The visual effect of automatic exposure is similar to how human visual perception adjusts to changes in environmental lighting. For example, consider a game scene where the player moves from a darkened area into full daylight. At first, the exposure value is low, allowing for visible detail in the darkened area, but no detail in the white daylight outside. As the player moves into the daylight, the entire view becomes blindingly bright, but over a brief time the player’s vision adapts: detail becomes visible in the bright area, and the darkened area loses detail.

If this property’s value is [`false`](https://developer.apple.com/documentation/swift/false), SceneKit’s tone mapping effect is constant. Instead of responding to scene luminance, SceneKit uses the [`averageGray`](scncamera/averagegray.md) property to determine the tone mapping curve.

This property has no effect if the [`wantsHDR`](scncamera/wantshdr.md) value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var exposureAdaptationBrighteningSpeedFactor: CGFloat](scncamera/exposureadaptationbrighteningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from dark to bright areas.
- [var exposureAdaptationDarkeningSpeedFactor: CGFloat](scncamera/exposureadaptationdarkeningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from bright to dark areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/wantsexposureadaptation)*