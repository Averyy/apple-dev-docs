# newTexture(URL:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads image data and creates a new Metal texture from a given URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]? = nil, completionHandler: @escaping @Sendable ((any MTLTexture)?, (any Error)?) -> Void)
```

```swift
func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> any MTLTexture
```

```objc
- (void) newTextureWithContentsOfURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options completionHandler:(MTKTextureLoaderCallback) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> MTLTexture
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `URL`: The URL of the file to load.
- `options`: A dictionary describing any additional texture loading steps. See `Texture Loading Options`.
- `completionHandler`: A block called when the texture has been loaded and fully initialized.

## See Also

### Loading Textures from URLs
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](./newtexture%28url,options%29.md)
  Synchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, error: NSErrorPointer) -> [any MTLTexture]](./newtextures%28urls,options,error%29.md)
  Synchronously loads image data and creates new Metal textures from the specified list of URLs.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](./newtextures%28urls,options,completionhandler%29.md)
  Asynchronously loads image data and creates new Metal textures from the specified list of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(url:options:completionhandler:))*