# texture(withContentsOfFile:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads a 2D texture image from a file and creates a new texture from the data.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func texture(withContentsOfFile path: String, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?, completionHandler block: @escaping @Sendable (GLKTextureInfo?, (any Error)?) -> Void)
```

```swift
func texture(withContentsOfFile path: String, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

```objc
- (void) textureWithContentsOfFile:(NSString *) path options:(NSDictionary<NSString *,NSNumber *> *) options queue:(dispatch_queue_t) queue completionHandler:(GLKTextureLoaderCallback) block;
```

#### Discussion

This method is identical to [`texture(withContentsOfFile:options:)`](./texture%28withcontentsoffile,options%29.md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `path`: A path to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See [Texture Loading Options](../texture-loading-options.md).
- `queue`: A dispatch queue that your block is called on when the task completes. If `NULL` is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

### Loading Textures from Files
- [class func texture(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](./texture%28withcontentsoffile,options%29.md)
  Loads a 2D texture image from a file and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsoffile:options:queue:completionhandler:))*