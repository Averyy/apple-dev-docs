# SKMutableTexture

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A texture whose contents can be dynamically updated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class SKMutableTexture
```

```objc
@interface SKMutableTexture : SKTexture
```

## Mentions

- [Loading and Using Textures](./loading-and-using-textures.md)

## Overview

Normally, SpriteKit textures ([`SKTexture`](./sktexture.md) objects) are static, meaning that once created, their contents cannot be changed. This is important because a static image can be more efficiently managed inside the graphics hardware. However, sometimes you need to be able to update the contents of a texture dynamically. In this case, you should use a mutable texture. Because there is a performance penalty for updating the texture’s contents, consider other options first. For example, you can render a texture in hardware using the [`texture(from:)`](./skview/texture%28from%29.md) method and a node tree.

To use this class, create a mutable texture using either one of its creation methods or those of its superclass. Then, when you need to update the mutable texture object’s contents, call the [`modifyPixelData(_:)`](./skmutabletexture/modifypixeldata%28_%29.md) method. Your block is called with the location of the texture in memory. Your block should update this texture and then return.

## Topics

### Creating an Empty Mutable Texture
- [init(size: CGSize, pixelFormat: Int32)](./skmutabletexture/init%28size,pixelformat%29.md)
  Initializes an empty texture with a specific size and format.
- [init(size: CGSize)](./skmutabletexture/init%28size%29.md)
  Initializes an empty texture with a specific size.
- [+ mutableTextureWithSize:](./skmutabletexture/mutabletexturewithsize_.md)
  Creates an empty texture with a specific size.
### Modifying a Mutable Texture’s Contents
- [func modifyPixelData((UnsafeMutableRawPointer?, Int) -> Void)](./skmutabletexture/modifypixeldata%28_%29.md)
  Modifies the contents of a mutable texture.

## Relationships

### Inherits From
- [SKTexture](./sktexture.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Textures
- [Maximizing Texture Performance](./maximizing-texture-performance.md)
  Speed up image display and enable more images to be displayed at one time.
- [class SKTexture](./sktexture.md)
  An image, decoded on the GPU, that can be used to render various SpriteKit objects.
- [class SKTextureAtlas](./sktextureatlas.md)
  A collection of textures optimized for storage and drawing performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture)*