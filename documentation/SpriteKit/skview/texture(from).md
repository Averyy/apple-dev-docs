# texture(from:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Renders the contents of a node tree and returns the rendered image as a texture.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func texture(from node: SKNode) -> SKTexture?
```

```objc
- (SKTexture *) textureFromNode:(SKNode *) node;
```

## Mentions

- [Creating a New Node By Rendering To a Texture](../creating-a-new-node-by-rendering-to-a-texture.md)
- [Loading and Using Textures](../loading-and-using-textures.md)

#### Return Value

A SpriteKit texture that holds the rendered image.

#### Discussion

The node being rendered does not need to appear in the view’s presented scene. The new texture is created with a size equal to the rectangle returned by the node’s [`calculateAccumulatedFrame()`](../sknode/calculateaccumulatedframe%28%29.md) method. If the node is not a scene node, it is rendered with a clear background color (`[``SKColor` `clear]`).

## Parameters

- `node`: The node object that is the root node of the tree you want to render to the texture.

## See Also

### Snapshotting Nodes to a Texture
- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](./texture%28from,crop%29.md)
  Renders a portion of a node’s contents and returns the rendered image as a texture.
- [Creating a New Node By Rendering To a Texture](../creating-a-new-node-by-rendering-to-a-texture.md)
  Render a portion of the node tree into a new texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/texture(from:))*