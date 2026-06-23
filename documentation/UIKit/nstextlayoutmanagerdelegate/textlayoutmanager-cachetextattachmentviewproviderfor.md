# textLayoutManager(_:cacheTextAttachmentViewProvider:for:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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