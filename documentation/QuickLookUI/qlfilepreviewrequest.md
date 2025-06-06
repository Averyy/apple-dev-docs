# QLFilePreviewRequest

**Framework**: Quick Look UI  
**Kind**: class

A Quick Look preview request that indicates the content to preview.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLFilePreviewRequest
```

#### Overview

The system provides a [`QLFilePreviewRequest`](qlfilepreviewrequest.md) to the [`providePreview(for:completionHandler:)`](qlpreviewingcontroller/providepreview(for:completionhandler:).md) method of your data-based Quick Look extension.

## Topics

### Inspecting the preview request
- [var fileURL: URL](qlfilepreviewrequest/fileurl.md)
  The URL that indicates the content to preview.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class QLPreviewProvider](qlpreviewprovider.md)
  A class that you subclass to provide a data-based Quick Look preview extension.
- [class QLPreviewReply](qlpreviewreply.md)
  The class you create when providing a data-based Quick Look preview extension.
- [class QLPreviewReplyAttachment](qlpreviewreplyattachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlfilepreviewrequest)*