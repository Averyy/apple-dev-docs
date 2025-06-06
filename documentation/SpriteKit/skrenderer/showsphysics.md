# showsPhysics

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view displays physics-related debugging information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var showsPhysics: Bool { get set }
```

#### Discussion

When this debugging option is enabled, each time a frame is rendered, an overlay image is drawn on top of your scene that shows the positions and shapes of any physics bodies visible in the scene.

## See Also

- [var showsNodeCount: Bool](skrenderer/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](skrenderer/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](skrenderer/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsFields: Bool](skrenderer/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/showsphysics)*