# focalBlurSampleCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of pixel samples SceneKit uses to create depth-of-field blur effects.

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
var focalBlurSampleCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger focalBlurSampleCount;
```

## Discussion

When the [`wantsDepthOfField`](./wantsdepthoffield.md) setting is enabled, SceneKit renders depth-of-field blur (also called *bokeh*) effects using a blur filter that samples multiple points in the image. Sampling a larger number of points produces a higher quality visual effect at a higher performance cost, and vice versa. The default sample count is 25.

## See Also

### Adding Depth-of-Field Effects
- [var wantsDepthOfField: Bool](./wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var focusDistance: CGFloat](./focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](./fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](./aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focalblursamplecount)*