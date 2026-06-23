# textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)

**Framework**: UIKit  
**Kind**: method

Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor attachment: NSTextAttachment) -> NSTextAttachmentViewProvider?
```

#### Return Value

A previously cached view provider, or `nil`.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `attachment`: The attachment to retrieve a cached view provider for.

## See Also

- [func textLayoutManager(NSTextLayoutManager, cacheTextAttachmentViewProvider: NSTextAttachmentViewProvider, for: NSTextAttachment)](nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:).md)
  Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:))*