# wantsDepthOfField

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.

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
var wantsDepthOfField: Bool { get set }
```

#### Discussion

This value is [`false`](https://developer.apple.com/documentation/Swift/false) by default, disabling depth-of-field effects.

Enabling this property causes SceneKit to render blur effects that model those created by a physical camera device (also known as ). That is, objects in the scene appear more or less blurry depending on their distance from the camera and the camera’s [`focusDistance`](scncamera/focusdistance.md), and the intensity and style of the blur effect depend on the [`fStop`](scncamera/fstop.md) and [`apertureBladeCount`](scncamera/aperturebladecount.md) properties.

> **Note**:  For best results, also enable the [`wantsHDR`](scncamera/wantshdr.md) property when using depth-of-field effects. High Dynamic Range rendering provides high contrast for distant bright points in the scene, creating more pronounced bokeh effects.

## See Also

- [var focusDistance: CGFloat](scncamera/focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](scncamera/fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](scncamera/aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](scncamera/focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/wantsdepthoffield)*