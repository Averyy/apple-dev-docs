# loadPreviewImage(options:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func loadPreviewImage(options: [AnyHashable : Any]! = [:], completionHandler: NSItemProvider.CompletionHandler!)
```

```swift
func loadPreviewImage(options: [AnyHashable : Any]! = [:]) async throws -> any NSSecureCoding
```

```objc
- (void) loadPreviewImageWithOptions:(NSDictionary *) options completionHandler:(NSItemProviderCompletionHandler) completionHandler;
```

## Discussion

To handle image preview yourself, provide a completion handler block that returns an [`NSData`](../nsdata.md) or [`NSURL`](../nsurl.md) object, or an instance of a platform-specific image class ([`UIImage`](../../UIKit/uiimage.md) or [`NSImage`](../../AppKit/nsimage.md)).

This method supports implicit type coercion for the item parameter of the completion block.

## Parameters

- `options`: A dictionary of keys and values that provide information about the item, such as the size of an image. For a list of possible keys, see [Options Dictionary Key](../options-dictionary-key.md).
- `completionHandler`: A completion handler block to execute with the results. The first parameter of this block must be a parameter of type [`NSData`](../nsdata.md), [`NSURL`](../nsurl.md), [`UIImage`](../../UIKit/uiimage.md) (in iOS), or [`NSImage`](../../AppKit/nsimage.md) (in macOS) for receiving the image data. For more information about implementing the block, see [`NSItemProvider.CompletionHandler`](./completionhandler.md).

## See Also

### Loading a preview image
- [var previewImageHandler: NSItemProvider.LoadHandler?](./previewimagehandler.md)
  The custom preview image handler block for the item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadpreviewimage(options:completionhandler:))*