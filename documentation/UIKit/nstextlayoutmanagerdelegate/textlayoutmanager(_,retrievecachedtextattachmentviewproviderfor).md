# textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor attachment: NSTextAttachment) -> NSTextAttachmentViewProvider?
```

```objc
- (NSTextAttachmentViewProvider *) textLayoutManager:(NSTextLayoutManager *) textLayoutManager retrieveCachedTextAttachmentViewProviderForTextAttachment:(NSTextAttachment *) attachment;
```

## Return Value

A previously cached view provider, or `nil`.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `attachment`: The attachment to retrieve a cached view provider for.

## See Also

### Reusing text attachment view providers
- [func textLayoutManager(NSTextLayoutManager, cacheTextAttachmentViewProvider: NSTextAttachmentViewProvider, for: NSTextAttachment)](./textlayoutmanager%28_,cachetextattachmentviewprovider,for%29.md)
  Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:))*