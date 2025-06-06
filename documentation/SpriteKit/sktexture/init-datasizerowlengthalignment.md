# init(data:size:rowLength:alignment:)

**Framework**: SpriteKit  
**Kind**: init

Creates a new texture from custom formatted raw pixel data.

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
convenience init(data pixelData: Data, size: CGSize, rowLength: UInt32, alignment: UInt32)
```

#### Return Value

A new texture object.

#### Discussion

The image data is copied before control is returned to your game.

## Parameters

- `pixelData`: An   object that holds the bitmap data. The pixels must be 32 bpp, 8bpc (unsigned integer) RGBA pixel data. The color components should have been already multiplied by the alpha value.
- `size`: The size of the new texture in points.
- `rowLength`: The number of bytes of memory to use per row of the bitmap.
- `alignment`: The offset between individual pixels of the pixel data. Specify   for tightly packed data.

## See Also

- [convenience init(data: Data, size: CGSize)](sktexture/init(data:size:).md)
  Creates a new texture from raw pixel data.
- [convenience init(data: Data, size: CGSize, flipped: Bool)](sktexture/init(data:size:flipped:).md)
  Creates a new texture from raw pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(data:size:rowlength:alignment:))*