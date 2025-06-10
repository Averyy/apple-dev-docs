# apertureBladeCount

**Framework**: SceneKit  
**Kind**: property

The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.

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
var apertureBladeCount: Int { get set }
```

#### Discussion

When the [`wantsDepthOfField`](scncamera/wantsdepthoffield.md) setting is enabled, SceneKit renders scenes using the camera with a depth-of-field blur (also called ) effect modeled after those created by a real-world physical camera. One feature of real-world camera bokeh effects is the tendency of distant bright points to blur into larger shapes based on the shape of the aperture between the camera’s lens and its imaging plane (film or sensor). Physical cameras control aperture using a mechanism that moves several flat blades in or out to create a smaller or larger opening, so the natural bokeh effect in traditional photography produces polygon-shaped blur effects.

This property controls the number of blades in the simulated camera aperture, and thus the polygon shape seen in the resulting bokeh effect. For example, a blade count of 6 (the default) causes distant bright points to blur into hexagon shapes. Increasingly large blade counts result in the bokeh effect appearing more circular, as shown below.

![Screenshots showing aperture blade count settings of 5, 6, and 10, resulting in differently-shaped blur effects for distant point lights.](https://docs-assets.developer.apple.com/published/af032325a768456a11e5715aa501c042/media-2953443%402x.png)

## See Also

- [var wantsDepthOfField: Bool](scncamera/wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var focusDistance: CGFloat](scncamera/focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](scncamera/fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var focalBlurSampleCount: Int](scncamera/focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/aperturebladecount)*