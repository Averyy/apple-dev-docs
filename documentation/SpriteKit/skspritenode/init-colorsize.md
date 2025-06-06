# init(color:size:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a single-color sprite node.

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
@MainActor
convenience init(color: UIColor, size: CGSize)
```

#### Return Value

A newly initialized sprite node.

#### Discussion

Although textured nodes are the most common way to use the [`SKSpriteNode`](skspritenode.md) class, you can also create sprite nodes without a texture. The behavior of the class changes when the node lacks a texture:

- The sprite node that is returned from this method has its [`texture`](skspritenode/texture.md) property set to `nil`.
- There is no texture to stretch, so the [`centerRect`](skspritenode/centerrect.md) parameter is ignored.
- There is no colorization step; the [`color`](skspritenode/color.md) property is used as the sprite’s color.
- The sprite node’s [`alpha`](sknode/alpha.md) component is used to determine how it is blended into the buffer.

Listing 1 shows how to create a red sprite node `100 x 100` points in size.

Listing 1. Creating a non-textured sprite node

```swift
let node = SKSpriteNode(color: .red,
                        size: CGSize(width: 100, height: 100))
```

## Parameters

- `color`: The color for the resulting sprite node.
- `size`: The size of the sprite node in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(color:size:))*