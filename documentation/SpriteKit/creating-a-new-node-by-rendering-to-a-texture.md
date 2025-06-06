# Creating a New Node By Rendering To a Texture

**Framework**: SpriteKit

Render a portion of the node tree into a new texture.

#### Overview

You can create a texture from some portion of on-screen content with [`texture(from:)`](skview/texture(from:).md), or its variation, [`texture(from:crop:)`](skview/texture(from:crop:).md). Both of these functions are available for scenes rendered by [`SKView`](skview.md) or [`WKInterfaceSKScene`](https://developer.apple.com/documentation/WatchKit/WKInterfaceSKScene).

There are a couple reasons you might want to do this, for example:

- Creating a new sprite node whose texture reflects prior shading done with [`SKShader`](skshader.md)
- Flattening a hierarchy of nodes into a texture, either for performance, or to apply some effect. Note that this can also be done using [`SKEffectNode`](skeffectnode.md) and setting [`shouldRasterize`](skeffectnode/shouldrasterize.md) to true.
- Breaking appart an existing node into separate nodes, for example, for an explosion effect.

## See Also

- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](skview/texture(from:crop:).md)
  Renders a portion of a node’s contents and returns the rendered image as a texture.
- [func texture(from: SKNode) -> SKTexture?](skview/texture(from:).md)
  Renders the contents of a node tree and returns the rendered image as a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-new-node-by-rendering-to-a-texture)*