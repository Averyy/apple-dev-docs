# texture(withContentsOfFile:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method

Asynchronously loads a 2D texture image from a file and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func texture(withContentsOfFile path: String, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

#### Discussion

This method is identical to [`texture(withContentsOfFile:options:)`](glktextureloader/texture(withcontentsoffile:options:).md), except that it loads the texture asynchronously. When this method is called, it creates a new background task to handle the request and then returns control to your app. Later, when the task is complete, GLKit calls your completion handler on the queue you provided.

## Parameters

- `path`: A path to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .
- `queue`: A dispatch queue that your block is called on when the task completes. If   is passed, the block is called on the main dispatch queue.
- `block`: A block to be called when the task completes.

## See Also

- [class func texture(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withcontentsoffile:options:).md)
  Loads a 2D texture image from a file and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsoffile:options:queue:completionhandler:))*