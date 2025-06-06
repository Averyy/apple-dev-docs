# anchorPoint

**Framework**: SpriteKit  
**Kind**: property

The point in the sprite that corresponds to the node’s position.

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
var anchorPoint: CGPoint { get set }
```

## Mentions

- [Adding a Video to a Scene](adding-a-video-to-a-scene.md)

#### Discussion

You specify the anchor point using the unit coordinate space. The default value is `(0.5,0.5)`, which means that the video is centered on the node’s position.

## See Also

- [var size: CGSize](skvideonode/size.md)
  The dimensions of the video node, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/anchorpoint)*