# init(data:size:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a new texture from raw pixel data.

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
convenience init(data pixelData: Data, size: CGSize)
```

```objc
+ (instancetype) textureWithData:(NSData *) pixelData size:(CGSize) size;
```

#### Return Value

A new texture object.

#### Discussion

The image data is copied before control is returned to your game.

Creating textures from raw pixel data is useful if you have a CPU based routine for creating imagery. The following Swift code shows how you can use [`init(data:size:)`](./init%28data,size%29.md) to create a texture containing random colors and a solid alpha. The `bytes` array is populated by iterating over the total number of pixels and adding four [`UInt8`](../../Swift/uint8.md) values for the red, green, blue, and alpha channels.

```swift
let width = 128
let height = 128
let bytes = stride(from: 0, to: width * height, by: 1).flatMap {
    _ in
    return [
        UInt8(drand48() * 255), // red
        UInt8(drand48() * 255), // green
        UInt8(drand48() * 255), // blue
        UInt8(255)              // alpha
    ]
}
let data = Data(bytes: bytes)
let texture = SKTexture(data: data,
                        size: CGSize(width: width, height: height))
```

## Parameters

- `pixelData`: An `NSData` object that holds the bitmap data. The pixels must be 32 bpp, 8bpc (unsigned integer) RGBA pixel data. The color components should have been already multiplied by the alpha value.
- `size`: The size of the new texture in points.

## See Also

### Texture from Data
- [convenience init(data: Data, size: CGSize, rowLength: UInt32, alignment: UInt32)](./init%28data,size,rowlength,alignment%29.md)
  Creates a new texture from custom formatted raw pixel data.
- [convenience init(data: Data, size: CGSize, flipped: Bool)](./init%28data,size,flipped%29.md)
  Creates a new texture from raw pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(data:size:))*