# previewImageHandler

**Framework**: Foundation  
**Kind**: property

The custom preview image handler block for the item provider.

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
var previewImageHandler: NSItemProvider.LoadHandler? { get set }
```

#### Discussion

In your image handler block, return an [`NSURL`](nsurl.md) object that specifies a file, or return an [`NSData`](nsdata.md) object.

## See Also

- [func loadPreviewImage(options: [AnyHashable : Any]!, completionHandler: NSItemProvider.CompletionHandler!)](nsitemprovider/loadpreviewimage(options:completionhandler:).md)
  Loads the preview image for the item that the item provider represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/previewimagehandler)*