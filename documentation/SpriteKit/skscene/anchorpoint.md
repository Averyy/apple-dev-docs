# anchorPoint

**Framework**: SpriteKit  
**Kind**: property

The point in the view’s frame that corresponds to the scene’s origin.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
var anchorPoint: CGPoint { get set }
```

## Mentions

- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
- [Getting Started with a Camera](getting-started-with-a-camera.md)
- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)

#### Discussion

When a scene is presented and a camera node has not been specified, the [`size`](skscene/size.md) and [`anchorPoint`](skscene/anchorpoint.md) properties determine which part of the scene’s coordinate space is visible in the view.

You specify the value using the unit coordinate space. The default value is `(0,0)`, which corresponds to the lower-left corner of the view’s frame rectangle.

## See Also

- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
  Try the different ways to configure the scene’s origin inside its view.
- [var camera: SKCameraNode?](skscene/camera.md)
  The camera node in the scene that determines what part of the scene’s coordinate space is visible in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/anchorpoint)*