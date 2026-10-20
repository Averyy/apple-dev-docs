# previewImageHandler

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (atomic, copy, nullable) NSItemProviderLoadHandler previewImageHandler;
```

#### Discussion

In your image handler block, return an [`NSURL`](../nsurl.md) object that specifies a file, or return an [`NSData`](../nsdata.md) object.

## See Also

### Loading a preview image
- [func loadPreviewImage(options: [AnyHashable : Any]!, completionHandler: NSItemProvider.CompletionHandler!)](./loadpreviewimage%28options,completionhandler%29.md)
  Loads the preview image for the item that the item provider represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/previewimagehandler)*