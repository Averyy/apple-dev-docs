# showsQuadCount

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsQuadCount: Bool { get set }
```

#### Discussion

SpriteKit converts the node tree into one or more rendering passes. Each rendering pass is rendered using a series of textured rectangles (quads). The [`showsQuadCount`](skview/showsquadcount.md) property allows you to see the total number of quads that were used to render the scene’s contents. Use this as another piece of data when you profile your game’s performance. In most cases, fewer quads is better.

## See Also

- [var showsFPS: Bool](skview/showsfps.md)
  A Boolean value that indicates whether the view displays a frame rate indicator.
- [var showsNodeCount: Bool](skview/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](skview/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsPhysics: Bool](skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/showsquadcount)*