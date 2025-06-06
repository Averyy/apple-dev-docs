# texture(from:)

**Framework**: SpriteKit  
**Kind**: method

Renders the contents of a node tree and returns the rendered image as a texture.

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
func texture(from node: SKNode) -> SKTexture?
```

## Mentions

- [Loading and Using Textures](loading-and-using-textures.md)
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)

#### Return Value

A SpriteKit texture that holds the rendered image.

#### Discussion

The node being rendered does not need to appear in the view’s presented scene. The new texture is created with a size equal to the rectangle returned by the node’s [`calculateAccumulatedFrame()`](sknode/calculateaccumulatedframe().md) method. If the node is not a scene node, it is rendered with a clear background color (`[``SKColor` `clear]`).

## Parameters

- `node`: The node object that is the root node of the tree you want to render to the texture.

## See Also

- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](skview/texture(from:crop:).md)
  Renders a portion of a node’s contents and returns the rendered image as a texture.
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)
  Render a portion of the node tree into a new texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/texture(from:))*