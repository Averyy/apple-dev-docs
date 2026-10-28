# focusDistance

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The distance from the camera at which objects appear in sharp focus. Animatable.

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
var focusDistance: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat focusDistance;
```

## Discussion

Objects at this distance from the camera appear perfectly focused. Objects nearer to or farther from the camera than this distance appear increasingly blurred, with the behavior of the blur effect depending on the [`fStop`](./fstop.md), [`apertureBladeCount`](./aperturebladecount.md) and [`focalBlurSampleCount`](./focalblursamplecount.md) properties. The default focus distance is `2.5`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adding Depth-of-Field Effects
- [var wantsDepthOfField: Bool](./wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var fStop: CGFloat](./fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](./aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](./focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focusdistance)*