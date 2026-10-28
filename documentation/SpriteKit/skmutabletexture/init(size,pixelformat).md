# init(size:pixelFormat:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes an empty texture with a specific size and format.

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
init(size: CGSize, pixelFormat format: Int32)
```

```objc
- (instancetype) initWithSize:(CGSize) size pixelFormat:(int) format;
```

## Return Value

An empty mutable texture.

## Discussion

You must call the [`modifyPixelData(_:)`](./modifypixeldata%28_%29.md) method at least once before using this texture.

## Parameters

- `size`: The size of the texture, in pixels.
- `format`: A Core Video format code. Three codes are supported: [`kCVPixelFormatType_32RGBA`](../../CoreVideo/kcvpixelformattype_32rgba.md), [`kCVPixelFormatType_64RGBAHalf`](../../CoreVideo/kcvpixelformattype_64rgbahalf.md), and [`kCVPixelFormatType_128RGBAFloat`](../../CoreVideo/kcvpixelformattype_128rgbafloat.md) for byte, half-float, and float components respectively.

## See Also

### Creating an Empty Mutable Texture
- [init(size: CGSize)](./init%28size%29.md)
  Initializes an empty texture with a specific size.
- [+ mutableTextureWithSize:](./mutabletexturewithsize_.md)
  Creates an empty texture with a specific size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture/init(size:pixelformat:))*