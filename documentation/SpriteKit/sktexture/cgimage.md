# cgImage()

**Framework**: SpriteKit  
**Kind**: method

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

#### Discussion

The [`cgImage()`](sktexture/cgimage().md) property returns the contents of a texture as a Quartz Image.

As an example use, you can create an image from a portion of your scene and save it to disk by doing the following:

1. Use the [`texture(from:)`](skview/texture(from:).md) method to render the scene’s contents to a texture.
2. Call [`cgImage()`](sktexture/cgimage().md) on the result.
3. Use [`CGImageDestination`](https://developer.apple.com/documentation/ImageIO/CGImageDestination) to write the `CGImage` out to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/cgimage())*