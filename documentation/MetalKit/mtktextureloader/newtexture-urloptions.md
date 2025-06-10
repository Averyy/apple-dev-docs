# newTexture(URL:options:)

**Framework**: MetalKit  
**Kind**: method

Synchronously loads image data and creates a new Metal texture from a given URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `URL`: The URL of the file to load.
- `options`: A dictionary describing any additional texture loading steps. See  .

## See Also

- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(url:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, error: NSErrorPointer) -> [any MTLTexture]](mtktextureloader/newtextures(urls:options:error:).md)
  Synchronously loads image data and creates new Metal textures from the specified list of URLs.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(urls:options:completionhandler:).md)
  Asynchronously loads image data and creates new Metal textures from the specified list of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(url:options:))*