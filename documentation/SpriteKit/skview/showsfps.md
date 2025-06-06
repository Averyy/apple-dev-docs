# showsFPS

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the view displays a frame rate indicator.

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
var showsFPS: Bool { get set }
```

#### Discussion

The frame rate is a good indicator of the performance of your scene. Avoid creating scenes that have widely varying frame rates.

## See Also

- [var showsNodeCount: Bool](skview/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](skview/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](skview/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/showsfps)*