# fogEndDistance

**Framework**: SceneKit  
**Kind**: property

The distance from a point of view at which the scene’s contents are completely obscured by fog. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var fogEndDistance: CGFloat { get set }
```

#### Discussion

A fog effect causes scene contents to become less visible the farther they are from the [`pointOfView`](scnscenerenderer/pointofview.md) node currently used for rendering. At distances less than the value of the [`fogStartDistance`](scnscene/fogstartdistance.md) property, scene contents are fully visible. At greater distances, SceneKit blends the rendered scene contents with a constant color (specified by the [`fogColor`](scnscene/fogcolor.md) property). At distances greater than the [`fogEndDistance`](scnscene/fogenddistance.md) property, the scene contents fade away completely and only the fog color is visible. Use fog to add atmospheric effects to your app or game, or to improve rendering performance by hiding parts of the scene that are far away from the current point of view.

The default end distance of `0.0` disables the fog effect. Change this property’s value to enable fog.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var fogStartDistance: CGFloat](scnscene/fogstartdistance.md)
  The distance from a point of view at which the scene’s contents begin to be obscured by fog. Animatable.
- [var fogDensityExponent: CGFloat](scnscene/fogdensityexponent.md)
  The transition curve for the fog’s intensity between its start and end distances. Animatable.
- [var fogColor: Any](scnscene/fogcolor.md)
  The color of the fog effect to be rendered with the scene. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/fogenddistance)*