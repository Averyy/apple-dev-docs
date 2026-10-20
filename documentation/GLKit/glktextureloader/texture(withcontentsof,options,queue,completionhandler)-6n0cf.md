# texture(withContentsOf:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads a 2D texture image from a memory range and creates a new texture from the data.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func texture(withContentsOf data: Data, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?, completionHandler block: @escaping @Sendable (GLKTextureInfo?, (any Error)?) -> Void)
```

```swift
func texture(withContentsOf data: Data, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

```objc
- (void) textureWithContentsOfData:(NSData *) data options:(NSDictionary<NSString *,NSNumber *> *) options queue:(dispatch_queue_t) queue completionHandler:(GLKTextureLoaderCallback) block;
```

#### Discussion

This method is identical to [`texture(withContentsOf:options:)`](./texture%28withcontentsof,options%29-2ljxb.md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `data`: The memory range to load as a texture.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See [Texture Loading Options](../texture-loading-options.md).
- `queue`: A dispatch queue that your block is called on when the task completes. If `NULL` is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

### Creating Textures from In-Memory Representations
- [class func texture(withContentsOf: Data, options: [String : NSNumber]?) throws -> GLKTextureInfo](./texture%28withcontentsof,options%29-2ljxb.md)
  Loads a 2D texture image from a memory range and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsof:options:queue:completionhandler:)-6n0cf)*