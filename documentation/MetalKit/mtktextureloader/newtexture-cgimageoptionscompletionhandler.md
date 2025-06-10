# newTexture(cgImage:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method

Asynchronously loads image data and creates a new Metal texture from a given bitmap image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> any MTLTexture
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> MTLTexture
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `cgImage`: The   from which to load image data.
- `options`: A dictionary describing any additional texture loading steps. See  .
- `completionHandler`: A block called when the texture has been loaded and fully initialized.

## See Also

- [func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(cgimage:options:).md)
  Synchronously loads image data and creates a new Metal texture from a given bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(cgimage:options:completionhandler:))*