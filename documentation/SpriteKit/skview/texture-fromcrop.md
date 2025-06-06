# texture(from:crop:)

**Framework**: SpriteKit  
**Kind**: method

Renders a portion of a node’s contents and returns the rendered image as a texture.

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
func texture(from node: SKNode, crop: CGRect) -> SKTexture?
```

## Mentions

- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)

#### Return Value

A SpriteKit texture that holds the rendered image.

#### Discussion

The node being rendered does not need to appear in the view’s presented scene. The new texture is created with a size equal to the size of the `crop` rectangle. If the node is not a scene node, it is rendered with a clear background color (`[``SKColor` `clear]`).

## Parameters

- `node`: The node object that is the root node of the tree you want to render to the texture.
- `crop`: A rectangle in the node’s coordinate system that describes the area to be rendered.

## See Also

- [func texture(from: SKNode) -> SKTexture?](skview/texture(from:).md)
  Renders the contents of a node tree and returns the rendered image as a texture.
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)
  Render a portion of the node tree into a new texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/texture(from:crop:))*