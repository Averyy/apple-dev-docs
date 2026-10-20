# cubeMap(withContentsOfFile:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func cubeMap(withContentsOfFile path: String, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?, completionHandler block: @escaping @Sendable (GLKTextureInfo?, (any Error)?) -> Void)
```

```swift
func cubeMap(withContentsOfFile path: String, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

```objc
- (void) cubeMapWithContentsOfFile:(NSString *) path options:(NSDictionary<NSString *,NSNumber *> *) options queue:(dispatch_queue_t) queue completionHandler:(GLKTextureLoaderCallback) block;
```

#### Discussion

This method is identical to [`cubeMap(withContentsOfFile:options:)`](./cubemap%28withcontentsoffile,options%29.md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `path`: A path to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See [Texture Loading Options](../texture-loading-options.md).
- `queue`: A dispatch queue that your block is called on when the task completes. If `NULL` is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

### Loading Cube Maps from Files
- [class func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](./cubemap%28withcontentsoffile,options%29.md)
  Loads a cube map texture image from a single file and creates a new texture from the data.
- [class func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo](./cubemap%28withcontentsoffiles,options%29.md)
  Loads a cube map texture image from a series of files and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./cubemap%28withcontentsoffiles,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/cubemap(withcontentsoffile:options:queue:completionhandler:))*