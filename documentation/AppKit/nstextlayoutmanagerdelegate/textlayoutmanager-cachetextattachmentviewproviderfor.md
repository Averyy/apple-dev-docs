# textLayoutManager(_:cacheTextAttachmentViewProvider:for:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.

**Availability**:
- macOS 27.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:))*