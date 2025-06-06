# focusDistance

**Framework**: SceneKit  
**Kind**: property

The distance from the camera at which objects appear in sharp focus. Animatable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var focusDistance: CGFloat { get set }
```

#### Discussion

Objects at this distance from the camera appear perfectly focused. Objects nearer to or farther from the camera than this distance appear increasingly blurred, with the behavior of the blur effect depending on the [`fStop`](scncamera/fstop.md), [`apertureBladeCount`](scncamera/aperturebladecount.md) and [`focalBlurSampleCount`](scncamera/focalblursamplecount.md) properties. The default focus distance is `2.5`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var wantsDepthOfField: Bool](scncamera/wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var fStop: CGFloat](scncamera/fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](scncamera/aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](scncamera/focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focusdistance)*