# newTextures(URLs:options:error:)

**Framework**: MetalKit  
**Kind**: method

Synchronously loads image data and creates new Metal textures from the specified list of URLs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]? = nil, error: NSErrorPointer) -> [any MTLTexture]
```

#### Return Value

An array of Metal textures, each corresponding to a URL listed in the `URLs` parameter. If an error occurs while loading a texture, the corresponding array element is an [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object.

## Parameters

- `URLs`: An array of URLs referencing files to load.
- `options`: A dictionary describing any additional texture loading steps. See  .
- `error`: If all textures were fully loaded and initialized, this pointer is   on output. If an error occurs while loading any of the specified URLs, this pointer refers to an   object describing the failure. (Which element in the   array the error corresponds to is undefined.)

## See Also

- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(url:options:).md)
  Synchronously loads image data and creates a new Metal texture from a given URL.
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?, completionHandler: MTKTextureLoader.Callback)](mtktextureloader/newtexture(url:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, completionHandler: MTKTextureLoader.ArrayCallback)](mtktextureloader/newtextures(urls:options:completionhandler:).md)
  Asynchronously loads image data and creates new Metal textures from the specified list of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtextures(urls:options:error:))*