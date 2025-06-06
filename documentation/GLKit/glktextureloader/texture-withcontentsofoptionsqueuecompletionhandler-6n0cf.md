# texture(withContentsOf:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method

Asynchronously loads a 2D texture image from a memory range and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func texture(withContentsOf data: Data, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

#### Discussion

This method is identical to [`texture(withContentsOf:options:)`](glktextureloader/texture(withcontentsof:options:)-2ljxb.md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `data`: The memory range to load as a texture.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .
- `queue`: A dispatch queue that your block is called on when the task completes. If   is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

- [class func texture(withContentsOf: Data, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withcontentsof:options:)-2ljxb.md)
  Loads a 2D texture image from a memory range and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsof:options:queue:completionhandler:)-6n0cf)*