# loadPreviewImage(options:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Loads the preview image for the item that the item provider represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func loadPreviewImage(options: [AnyHashable : Any]! = [:]) async throws -> any NSSecureCoding
```

#### Discussion

To handle image preview yourself, provide a completion handler block that returns an [`NSData`](nsdata.md) or [`NSURL`](nsurl.md) object, or an instance of a platform-specific image class ([`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) or [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage)).

This method supports implicit type coercion for the item parameter of the completion block.

## Parameters

- `options`: A dictionary of keys and values that provide information about the item, such as the size of an image. For a list of possible keys, see  .
- `completionHandler`: A completion handler block to execute with the results. The first parameter of this block must be a parameter of type  ,  ,   (in iOS), or   (in macOS) for receiving the image data. For more information about implementing the block, see  .

## See Also

- [var previewImageHandler: NSItemProvider.LoadHandler?](nsitemprovider/previewimagehandler.md)
  The custom preview image handler block for the item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadpreviewimage(options:completionhandler:))*