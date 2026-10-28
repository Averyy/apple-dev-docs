# init(data:size:rowLength:alignment:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a new texture from custom formatted raw pixel data.

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
convenience init(data pixelData: Data, size: CGSize, rowLength: UInt32, alignment: UInt32)
```

```objc
+ (instancetype) textureWithData:(NSData *) pixelData size:(CGSize) size rowLength:(unsigned int) rowLength alignment:(unsigned int) alignment;
```

## Return Value

A new texture object.

## Discussion

The image data is copied before control is returned to your game.

## Parameters

- `pixelData`: An `NSData` object that holds the bitmap data. The pixels must be 32 bpp, 8bpc (unsigned integer) RGBA pixel data. The color components should have been already multiplied by the alpha value.
- `size`: The size of the new texture in points.
- `rowLength`: The number of bytes of memory to use per row of the bitmap.
- `alignment`: The offset between individual pixels of the pixel data. Specify `0` for tightly packed data.

## See Also

### Texture from Data
- [convenience init(data: Data, size: CGSize)](./init%28data,size%29.md)
  Creates a new texture from raw pixel data.
- [convenience init(data: Data, size: CGSize, flipped: Bool)](./init%28data,size,flipped%29.md)
  Creates a new texture from raw pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(data:size:rowlength:alignment:))*