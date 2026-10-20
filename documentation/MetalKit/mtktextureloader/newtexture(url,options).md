# newTexture(URL:options:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id<MTLTexture>) newTextureWithContentsOfURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options error:(NSError **) error;
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `URL`: The URL of the file to load.
- `options`: A dictionary describing any additional texture loading steps. See `Texture Loading Options`.

## See Also

### Loading Textures from URLs
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28url,options,completionhandler%29.md)
  Asynchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, error: NSErrorPointer) -> [any MTLTexture]](./newtextures%28urls,options,error%29.md)
  Synchronously loads image data and creates new Metal textures from the specified list of URLs.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](./newtextures%28urls,options,completionhandler%29.md)
  Asynchronously loads image data and creates new Metal textures from the specified list of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(url:options:))*