# Maximizing Node Drawing Performance

**Framework**: SpriteKit

Structure your nodes for maximum performance.

#### Overview

As a high-level graphics framework, you configure your scene by laying out nodes, and `SpriteKit` builds the [`Metal`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/WhatsNewIniOS/Articles/iOS10.html#//apple_ref/doc/uid/TP40017084-SW36) draw calls for you that actually render the content. Thus, you have little control over the amount of low-level graphics work that SpriteKit does, but this article gives you hints that can speed up SpriteKit’s efforts.

##### Show Draw Count

Each draw call is an expensive operation; the more graphical elements you can pack into a single draw, the faster your scene can be rendered, and thus the higher frames per second it can achieve.

You can see the number of draw calls it’s taking to render your scene live on the `SKView` by enabling [`showsDrawCount`](skview/showsdrawcount.md).

In general, all scene nodes can be rendered in a single draw call that came from the same [`SKTexture`](sktexture.md), for example:

- Sprite nodes that use the same `SKTexture`
- Sprite nodes whose texture specifies a subrectangle of the same texture through the `SKTexture` [`init(rect:in:)`](sktexture/init(rect:in:).md).

In general, all nodes can be rendered in a single draw call that came from the same [`SKTextureAtlas`](sktextureatlas.md) using [`textureNamed(_:)`](sktextureatlas/texturenamed(_:).md).

> ❗ **Important**:  Node [`zPosition`](sknode/zposition.md) impacts draw call count because, generally, nodes at different `zPositions` must be rendered on a subsequent pass. For example, nodes that overlap each other must be done in separate draw calls. Overlapping nodes at the same `zPosition` can be rendered in the same draw call if you enable the `SKView` [`ignoresSiblingOrder`](skview/ignoressiblingorder.md) property.

For all other SpriteKit nodes that draw, pay attention to the [`showsDrawCount`](skview/showsdrawcount.md) statistic  as you develop your app to gain an understanding of which configurations affect draw count.

##### Show Node Count

The number of nodes in your scene relates to the number of draw calls. Therefore, minimizing the number of nodes in your scene is a good practice to keep the draw call count down. Showing the node count in your scene is done through the `SKView` [`showsNodeCount`](skview/showsnodecount.md) property.

The number of nodes in your scene can also affect performance if you enumerate all of your nodes within the update life cycle. While the `SKView` [`shouldCullNonVisibleNodes`](skview/shouldcullnonvisiblenodes.md) property can prune offscreen nodes out of an issued draw call, SpriteKit must still enumerate all nodes in your scene to figure out which ones are offscreen, and this is an expensive operation. As a result, eliminating offscreen nodes yourself by using [`removeFromParent()`](sknode/removefromparent().md) is the fastest way to cull nonvisible nodes. Once a node is removed from the node tree, `SpriteKit` no longer needs to consider whether it’s onscreen or offscreen every frame.

## See Also

- [class SKSpriteNode](skspritenode.md)
  An image or solid color.
- [class SKShapeNode](skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](skemitternode.md)
  A source of various particle effects.
- [class SKLabelNode](sklabelnode.md)
  A graphical element that draws text.
- [class SKVideoNode](skvideonode.md)
  A graphical element that plays video content.
- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/maximizing-node-drawing-performance)*