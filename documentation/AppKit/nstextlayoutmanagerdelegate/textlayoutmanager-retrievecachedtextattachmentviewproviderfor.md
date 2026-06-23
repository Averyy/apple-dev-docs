# textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)

**Framework**: AppKit  
**Kind**: method

Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor attachment: NSTextAttachment) -> NSTextAttachmentViewProvider?
```

#### Return Value

A previously cached view provider, or `nil`.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `attachment`: The attachment to retrieve a cached view provider for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:))*