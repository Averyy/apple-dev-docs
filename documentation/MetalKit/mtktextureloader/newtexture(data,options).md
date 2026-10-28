# newTexture(data:options:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

Synchronously creates a new Metal texture from an in-memory representation of the texture’s data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(data: Data, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

```objc
- (id<MTLTexture>) newTextureWithData:(NSData *) data options:(NSDictionary<NSString *,id> *) options error:(NSError **) error;
```

## Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `data`: The [`NSData`](../../Foundation/nsdata.md) object containing image data.
- `options`: A dictionary describing any additional texture loading steps. See `Texture Loading Options`.

## See Also

### Loading Textures from In-Memory Data Representations
- [func newTexture(data: Data, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28data,options,completionhandler%29.md)
  Asynchronously creates a new Metal texture from an in-memory representation of the texture’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(data:options:))*