# fStop

**Framework**: SceneKit  
**Kind**: property

The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.

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
var fStop: CGFloat { get set }
```

#### Discussion

F-stop numbers describe the light-gathering area of a physical camera’s imaging system, and are typically expressed as the denominator of a ratio including the camera’s focal length ƒ, such as ƒ/2 or ƒ/5.6. A larger denominator indicates a smaller aperture, allowing less light to pass from the camera’s lens through to the imaging plane (sensor or film), and a smaller denominator indicates a larger aperture that lets more light through.

SceneKit uses aperture measurements to simulate depth-of-field blur effects (also called ) approximating those produced by a physical camera. A larger [`fStop`](scncamera/fstop.md) number (or aperture denominator) causes most of the scene to appear in focus, with extremely close or far depths showing slight blurring; a smaller number results in only a narrow range of depths appearing in focus, and a more pronounced blur effect for the rest of the scene. The default [`fStop`](scncamera/fstop.md) value is `5.6`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var wantsDepthOfField: Bool](scncamera/wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var focusDistance: CGFloat](scncamera/focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var apertureBladeCount: Int](scncamera/aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](scncamera/focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/fstop)*