# maximumExposure

**Framework**: SceneKit  
**Kind**: property

The minimum exposure value to use in tone mapping.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var maximumExposure: CGFloat { get set }
```

#### Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called  to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. SceneKit determines a tone mapping curve from the [`minimumExposure`](scncamera/minimumexposure.md), [`maximumExposure`](scncamera/maximumexposure.md), [`exposureOffset`](scncamera/exposureoffset.md), and [`whitePoint`](scncamera/whitepoint.md) properties, along with a measure of scene luminance.

Exposure values are exponential: a value of `1.0` doubles brightness, a value of `2.0` quadruples brightness, a value of `-1.0` halves brightness, and so on. The default value is `15.0`. Decreasing the value causes brighter portions of the scene to become over-exposed (uniformly white, losing definition). Increasing the value adds more dynamic range for brighter portions of the scene; however, a greater breadth of difference between the minimum and maximum exposures decreases contrast.

This property has no effect if the [`wantsHDR`](scncamera/wantshdr.md) value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var wantsHDR: Bool](scncamera/wantshdr.md)
  A Boolean value that determines whether SceneKit applies High Dynamic Range (HDR) postprocessing effects to a scene.
- [var exposureOffset: CGFloat](scncamera/exposureoffset.md)
  A logarithmic bias that adjusts the results of SceneKit’s tone mapping operation, brightening or darkening the visible scene.
- [var averageGray: CGFloat](scncamera/averagegray.md)
  The luminance level to use as the midpoint of a tone mapping curve.
- [var whitePoint: CGFloat](scncamera/whitepoint.md)
  The luminance level to use as the upper end of a tone mapping curve.
- [var minimumExposure: CGFloat](scncamera/minimumexposure.md)
  The minimum exposure value to use in tone mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/maximumexposure)*