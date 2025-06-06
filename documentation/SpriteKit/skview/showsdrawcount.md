# showsDrawCount

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var showsDrawCount: Bool { get set }
```

## Mentions

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)

#### Discussion

Some operations in SpriteKit can require multiple rendering passes to draw a scene’s content. For example, an [`SKEffectNode`](skeffectnode.md) object must render its children into a separate buffer, apply the effect, and then perform another pass to blend those results into its parent node. These additional rendering passes use more rendering resources, reducing your game’s frame rate or increasing its total power consumption.  Use the draw count as another piece of data when you profile your game’s performance.

## See Also

- [var showsFPS: Bool](skview/showsfps.md)
  A Boolean value that indicates whether the view displays a frame rate indicator.
- [var showsNodeCount: Bool](skview/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsQuadCount: Bool](skview/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/showsdrawcount)*