# newTexture(texture:options:)

**Framework**: MetalKit  
**Kind**: method

Synchronously loads image data and creates a Metal texture from the specified Model I/O texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `texture`: A Model I/O texture object containing image data from which to create the texture.
- `options`: A dictionary describing any additional texture loading steps. See  .

## See Also

- [func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]?, completionHandler: MTKTextureLoader.Callback)](mtktextureloader/newtexture(texture:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the specified Model I/O texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(texture:options:))*