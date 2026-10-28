# init(cgImage:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Create a new texture object from a Quartz 2D image.

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
convenience init(cgImage image: CGImage)
```

```objc
+ (instancetype) textureWithCGImage:(CGImageRef) image;
```

## Return Value

A new texture object.

## Discussion

The image data is copied before control is returned to your game.

## Parameters

- `image`: A Quartz 2D image ([`CGImage`](../../CoreGraphics/cgimage.md)) object. For more information, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGImage`](../../CoreGraphics/cgimage.md).

## See Also

### Texture from Image
- [convenience init(image: UIImage)](./init%28image%29.md)
  Create a new texture object from an image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(cgimage:)-27ovb)*