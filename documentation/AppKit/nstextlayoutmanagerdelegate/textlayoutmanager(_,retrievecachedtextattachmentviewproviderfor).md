# textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor attachment: NSTextAttachment) -> NSTextAttachmentViewProvider?
```

```objc
- (NSTextAttachmentViewProvider *) textLayoutManager:(NSTextLayoutManager *) textLayoutManager retrieveCachedTextAttachmentViewProviderForTextAttachment:(NSTextAttachment *) attachment;
```

#### Return Value

A previously cached view provider, or `nil`.

## Parameters

- `textLayoutManager`: The text layout manager sending the message.
- `attachment`: The attachment to retrieve a cached view provider for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:))*