# showsDrawCount

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var showsDrawCount: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsDrawCount;
```

## Discussion

Some operations in SpriteKit can require multiple rendering passes to draw a scene’s content. For example, an [`SKEffectNode`](../skeffectnode.md) object must render its children into a separate buffer, apply the effect, and then perform another pass to blend those results into its parent node. These additional rendering passes use more rendering resources, reducing your game’s frame rate or increasing its total power consumption. Use the draw count as another piece of data when you profile your game’s performance.

## See Also

### Enabling Visual Statistics for Debugging
- [var showsNodeCount: Bool](./showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsQuadCount: Bool](./showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](./showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](./showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/showsdrawcount)*