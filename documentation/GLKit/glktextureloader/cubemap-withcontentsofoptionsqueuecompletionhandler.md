# cubeMap(withContentsOf:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method

Asynchronously loads a cube map texture image from a single URL and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func cubeMap(withContentsOf url: URL, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

#### Discussion

This method is identical to [`cubeMap(withContentsOf:options:)`](glktextureloader/cubemap(withcontentsof:options:).md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `url`: A path to the image to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .
- `queue`: A dispatch queue that your block is called on when the task completes. If   is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

- [class func cubeMap(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsof:options:).md)
  Loads a cube map texture image from a single URL and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/cubemap(withcontentsof:options:queue:completionhandler:))*