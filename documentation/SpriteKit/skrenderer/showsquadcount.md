# showsQuadCount

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var showsQuadCount: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsQuadCount;
```

#### Discussion

SpriteKit converts the node tree into one or more rendering passes. Each rendering pass is rendered using a series of textured rectangles (quads). The showsQuadCount property allows you to see the total number of quads that were used to render the scene’s contents. Use this as another piece of data when you profile your game’s performance. In most cases, fewer quads is better.

## See Also

### Enabling Visual Statistics for Debugging
- [var showsNodeCount: Bool](./showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](./showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsPhysics: Bool](./showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](./showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/showsquadcount)*