# showsNodeCount

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL showsNodeCount;
```

#### Discussion

When you enable this option, it shows the number of nodes currently in the scene’s node tree.

> **Note**:  The [`shouldCullNonVisibleNodes`](./shouldcullnonvisiblenodes.md) property affects how many nodes in the node tree are included in SpriteKit’s render pass but it doesn’t affect the [`showsNodeCount`](./showsnodecount.md) statistic.

You may achieve additional performance gain by actually removing nodes from the node tree manually which are off screen. For example, in the case of [`shouldCullNonVisibleNodes`](./shouldcullnonvisiblenodes.md), there would be less nodes for SpriteKit to test every frame whether they’re on screen.

## See Also

### Enabling Visual Statistics for Debugging
- [var showsDrawCount: Bool](./showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](./showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](./showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](./showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/showsnodecount)*