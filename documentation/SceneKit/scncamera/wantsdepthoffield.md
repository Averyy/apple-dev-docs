# wantsDepthOfField

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.

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
var wantsDepthOfField: Bool { get set }
```

```objc
@property (nonatomic) BOOL wantsDepthOfField;
```

## Discussion

This value is [`false`](../../Swift/false.md) by default, disabling depth-of-field effects.

Enabling this property causes SceneKit to render blur effects that model those created by a physical camera device (also known as *bokeh*). That is, objects in the scene appear more or less blurry depending on their distance from the camera and the camera’s [`focusDistance`](./focusdistance.md), and the intensity and style of the blur effect depend on the [`fStop`](./fstop.md) and [`apertureBladeCount`](./aperturebladecount.md) properties.

> **Note**:  For best results, also enable the [`wantsHDR`](./wantshdr.md) property when using depth-of-field effects. High Dynamic Range rendering provides high contrast for distant bright points in the scene, creating more pronounced bokeh effects.

## See Also

### Adding Depth-of-Field Effects
- [var focusDistance: CGFloat](./focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](./fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](./aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](./focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/wantsdepthoffield)*