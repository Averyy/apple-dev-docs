# showsNodeCount

**Framework**: Spritekit  
**Kind**: property

A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.

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
var showsNodeCount: Bool { get set }
```

## Mentions

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)

#### Discussion

When you enable this option, it shows the number of nodes currently in the scene’s node tree.

> **Note**:  The[`shouldCullNonVisibleNodes`](skview/shouldcullnonvisiblenodes.md) property affects how many nodes in the node tree are included in SpriteKit’s render pass but it doesn’t affect the [`showsNodeCount`](skview/showsnodecount.md) statistic.

You may achieve additional performance gain by actually removing nodes from the node tree manually which are off screen. For example, in the case of [`shouldCullNonVisibleNodes`](skview/shouldcullnonvisiblenodes.md), there would be less nodes for SpriteKit to test every frame whether they’re on screen.

## See Also

- [var showsFPS: Bool](skview/showsfps.md)
  A Boolean value that indicates whether the view displays a frame rate indicator.
- [var showsDrawCount: Bool](skview/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](skview/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/showsnodecount)*