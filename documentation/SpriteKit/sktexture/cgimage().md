# cgImage()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns the texture’s image data as a Quartz 2D image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cgImage() -> CGImage
```

```objc
- (CGImageRef) CGImage;
```

#### Discussion

The [`cgImage()`](./cgimage%28%29.md) property returns the contents of a texture as a Quartz Image.

As an example use, you can create an image from a portion of your scene and save it to disk by doing the following:

1. Use the [`texture(from:)`](../skview/texture%28from%29.md) method to render the scene’s contents to a texture.
2. Call [`cgImage()`](./cgimage%28%29.md) on the result.
3. Use [`CGImageDestination`](../../ImageIO/cgimagedestination.md) to write the `CGImage` out to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/cgimage())*