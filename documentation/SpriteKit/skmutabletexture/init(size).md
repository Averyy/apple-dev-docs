# init(size:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes an empty texture with a specific size.

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
init(size: CGSize)
```

```objc
- (instancetype) initWithSize:(CGSize) size;
```

#### Return Value

An empty mutable texture.

#### Discussion

You must call the [`modifyPixelData(_:)`](./modifypixeldata%28_%29.md) method at least once before using this texture.

## Parameters

- `size`: The size of the texture, in pixels.

## See Also

### Creating an Empty Mutable Texture
- [init(size: CGSize, pixelFormat: Int32)](./init%28size,pixelformat%29.md)
  Initializes an empty texture with a specific size and format.
- [+ mutableTextureWithSize:](./mutabletexturewithsize_.md)
  Creates an empty texture with a specific size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture/init(size:))*