# apertureBladeCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.

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
var apertureBladeCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger apertureBladeCount;
```

#### Discussion

When the [`wantsDepthOfField`](./wantsdepthoffield.md) setting is enabled, SceneKit renders scenes using the camera with a depth-of-field blur (also called *bokeh*) effect modeled after those created by a real-world physical camera. One feature of real-world camera bokeh effects is the tendency of distant bright points to blur into larger shapes based on the shape of the aperture between the camera’s lens and its imaging plane (film or sensor). Physical cameras control aperture using a mechanism that moves several flat blades in or out to create a smaller or larger opening, so the natural bokeh effect in traditional photography produces polygon-shaped blur effects.

This property controls the number of blades in the simulated camera aperture, and thus the polygon shape seen in the resulting bokeh effect. For example, a blade count of 6 (the default) causes distant bright points to blur into hexagon shapes. Increasingly large blade counts result in the bokeh effect appearing more circular, as shown below.

![Screenshots showing aperture blade count settings of 5, 6, and 10, resulting in differently-shaped blur effects for distant point lights.](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2953443@2x.png)

## See Also

### Adding Depth-of-Field Effects
- [var wantsDepthOfField: Bool](./wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var focusDistance: CGFloat](./focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](./fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var focalBlurSampleCount: Int](./focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/aperturebladecount)*