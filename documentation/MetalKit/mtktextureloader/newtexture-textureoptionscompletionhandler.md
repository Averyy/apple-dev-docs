# newTexture(texture:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method

Asynchronously loads image data and creates a Metal texture from the specified Model I/O texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> any MTLTexture
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> MTLTexture
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `texture`: A Model I/O texture object containing image data from which to create the texture.
- `options`: A dictionary describing any additional texture loading steps. See  .
- `completionHandler`: A block called when the texture has been loaded and fully initialized.

## See Also

- [func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(texture:options:).md)
  Synchronously loads image data and creates a Metal texture from the specified Model I/O texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(texture:options:completionhandler:))*