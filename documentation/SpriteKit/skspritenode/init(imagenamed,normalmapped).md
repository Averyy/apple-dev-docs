# init(imageNamed:normalMapped:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a textured sprite using an image file, optionally adding a normal map to simulate 3D lighting.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool)
```

```objc
+ (instancetype) spriteNodeWithImageNamed:(NSString *) name normalMapped:(BOOL) generateNormalMap;
```

#### Return Value

A newly initialized sprite object.

#### Discussion

The normal map is used only when lighting is enabled in the scene. For more information, see [`SKSpriteNode`](../skspritenode.md) and [`SKLightNode`](../sklightnode.md).

## Parameters

- `name`: The name of an image file stored in the app bundle.
- `generateNormalMap`: If [`true`](../../Swift/true.md), a normal map is generated from the image texture without applying any filter to it (SKTextureNormalMapFilteringTypeNone). If [`false`](../../Swift/false.md), no normal map is generated (matching the behavior of the [`spriteNodeWithImageNamed:`](./spritenodewithimagenamed_.md) class method).

## See Also

### Creating a Sprite from an Image Filename
- [Getting Started with Sprite Nodes](../getting-started-with-sprite-nodes.md)
  Learn the basics about using images, also known as sprites, with SpriteKit.
- [convenience init(imageNamed: String)](./init%28imagenamed%29.md)
  Initializes a textured sprite using an image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(imagenamed:normalmapped:))*