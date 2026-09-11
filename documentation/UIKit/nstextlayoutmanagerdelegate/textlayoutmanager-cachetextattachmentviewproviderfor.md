# textLayoutManager(_:cacheTextAttachmentViewProvider:for:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, cacheTextAttachmentViewProvider viewProvider: NSTextAttachmentViewProvider, for textAttachment: NSTextAttachment)
```

#### Discussion

The delegate can use this to cache the view provider.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `viewProvider`: The view provider being invalidated.
- `textAttachment`: The attachment associated with the view provider.

## See Also

- [func textLayoutManager(NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor: NSTextAttachment) -> NSTextAttachmentViewProvider?](nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:).md)
  Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:))*