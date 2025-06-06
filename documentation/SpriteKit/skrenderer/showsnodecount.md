# showsNodeCount

**Framework**: Spritekit  
**Kind**: property

A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var showsNodeCount: Bool { get set }
```

#### Discussion

When you enable this option, it shows the number of nodes currently in the scene’s node tree.

> **Note**:  The [`shouldCullNonVisibleNodes`](skrenderer/shouldcullnonvisiblenodes.md) property affects how many nodes in the node tree are included in SpriteKit’s render pass but it doesn’t affect the [`showsNodeCount`](skrenderer/showsnodecount.md) statistic.

You may achieve additional performance gain by actually removing nodes from the node tree manually which are off screen. For example, in the case of [`shouldCullNonVisibleNodes`](skrenderer/shouldcullnonvisiblenodes.md), there would be less nodes for SpriteKit to test every frame whether they’re on screen.

## See Also

- [var showsDrawCount: Bool](skrenderer/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](skrenderer/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](skrenderer/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skrenderer/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/showsnodecount)*