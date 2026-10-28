# init(textures:size:timePerFrame:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new tile definition with an array of textures for animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(textures: [SKTexture], size: CGSize, timePerFrame: CGFloat)
```

```objc
- (instancetype) initWithTextures:(NSArray<SKTexture *> *) textures size:(CGSize) size timePerFrame:(CGFloat) timePerFrame;
```

## Return Value

A new tile definition.

## Parameters

- `textures`: An array of textures to reference for the definition’s size and content.
- `size`: The size of the tile in points.
- `timePerFrame`: The duration, in seconds, that each texture is displayed.

## See Also

### Creating an Animated Tile
- [init(textures: [SKTexture], normalTextures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](./init%28textures,normaltextures,size,timeperframe%29.md)
  Initializes a new tile definition with arrays of textures and normal textures for animation.
- [+ tileDefinitionWithTextures:normalTextures:size:timePerFrame:](./tiledefinitionwithtextures_normaltextures_size_timeperframe_.md)
- [+ tileDefinitionWithTextures:size:timePerFrame:](./tiledefinitionwithtextures_size_timeperframe_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition/init(textures:size:timeperframe:))*