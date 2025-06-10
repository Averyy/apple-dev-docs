# newTextures(URLs:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method

Asynchronously loads image data and creates new Metal textures from the specified list of URLs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [any MTLTexture]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [MTLTexture]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `URLs`: An array of URLs referencing files to load.
- `options`: A dictionary describing any additional texture loading steps. See  .
- `completionHandler`: A block called after all URLs have been processed. See the   signature to determine whether each texture has successfully loaded.

## See Also

- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(url:options:).md)
  Synchronously loads image data and creates a new Metal texture from a given URL.
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(url:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, error: NSErrorPointer) -> [any MTLTexture]](mtktextureloader/newtextures(urls:options:error:).md)
  Synchronously loads image data and creates new Metal textures from the specified list of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtextures(urls:options:completionhandler:))*