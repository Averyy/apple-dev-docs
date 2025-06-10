# newTexture(cgImage:options:)

**Framework**: MetalKit  
**Kind**: method

Synchronously loads image data and creates a new Metal texture from a given bitmap image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `cgImage`: The   from which to load image data.
- `options`: A dictionary describing any additional texture loading steps. See  .

## See Also

- [func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(cgimage:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(cgimage:options:))*