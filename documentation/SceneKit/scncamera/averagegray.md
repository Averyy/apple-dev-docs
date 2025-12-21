# averageGray

**Framework**: SceneKit  
**Kind**: property

The luminance level to use as the midpoint of a tone mapping curve.

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
var averageGray: CGFloat { get set }
```

#### Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called  to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. SceneKit determines a tone mapping curve from the [`minimumExposure`](scncamera/minimumexposure.md), [`maximumExposure`](scncamera/maximumexposure.md), [`exposureOffset`](scncamera/exposureoffset.md), and [`whitePoint`](scncamera/whitepoint.md) properties, along with this property which serves as a constant estimate of scene luminance.

The default value is `0.18`. By setting this property to a higher or lower value, you can compensate for scenes with darker or brighter content. Alternatively, by setting the [`wantsExposureAdaptation`](scncamera/wantsexposureadaptation.md) property, you can allow SceneKit to automatically adjust exposure as the visible contents of the scene change.

This property has no effect if the [`wantsHDR`](scncamera/wantshdr.md) value is [`false`](https://developer.apple.com/documentation/Swift/false). If the [`exposureAdaptationDarkeningSpeedFactor`](scncamera/exposureadaptationdarkeningspeedfactor.md) value is [`true`](https://developer.apple.com/documentation/Swift/true), SceneKit ignores this property, and instead computes the average luminance currently visible to the camera during rendering.

## See Also

- [var wantsHDR: Bool](scncamera/wantshdr.md)
  A Boolean value that determines whether SceneKit applies High Dynamic Range (HDR) postprocessing effects to a scene.
- [var exposureOffset: CGFloat](scncamera/exposureoffset.md)
  A logarithmic bias that adjusts the results of SceneKit’s tone mapping operation, brightening or darkening the visible scene.
- [var whitePoint: CGFloat](scncamera/whitepoint.md)
  The luminance level to use as the upper end of a tone mapping curve.
- [var minimumExposure: CGFloat](scncamera/minimumexposure.md)
  The minimum exposure value to use in tone mapping.
- [var maximumExposure: CGFloat](scncamera/maximumexposure.md)
  The minimum exposure value to use in tone mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/averagegray)*