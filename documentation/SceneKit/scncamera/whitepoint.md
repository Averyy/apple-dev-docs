# whitePoint

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The luminance level to use as the upper end of a tone mapping curve.

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
var whitePoint: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat whitePoint;
```

## Discussion

When using a High Dynamic Range (HDR) camera, SceneKit applies a process called *tone mapping* to translate the wide range of luminance values in the visible scene to the narrower range of brightness values that can be shown on a display. SceneKit determines a tone mapping curve from the [`minimumExposure`](./minimumexposure.md), [`maximumExposure`](./maximumexposure.md), [`exposureOffset`](./exposureoffset.md), and [`whitePoint`](./whitepoint.md) properties, along with a measure of scene luminance.

The default value is `1.0`. By setting this property to a higher or lower value, you can produce more gradual or more abrupt transitions between shadows and highlights.

This property has no effect if the [`wantsHDR`](./wantshdr.md) value is [`false`](../../Swift/false.md).

## See Also

### Adding High Dynamic Range Effects
- [var wantsHDR: Bool](./wantshdr.md)
  A Boolean value that determines whether SceneKit applies High Dynamic Range (HDR) postprocessing effects to a scene.
- [var exposureOffset: CGFloat](./exposureoffset.md)
  A logarithmic bias that adjusts the results of SceneKit’s tone mapping operation, brightening or darkening the visible scene.
- [var averageGray: CGFloat](./averagegray.md)
  The luminance level to use as the midpoint of a tone mapping curve.
- [var minimumExposure: CGFloat](./minimumexposure.md)
  The minimum exposure value to use in tone mapping.
- [var maximumExposure: CGFloat](./maximumexposure.md)
  The minimum exposure value to use in tone mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/whitepoint)*