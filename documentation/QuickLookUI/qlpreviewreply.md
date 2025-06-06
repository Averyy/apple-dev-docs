# QLPreviewReply

**Framework**: Quick Look UI  
**Kind**: class

The class you create when providing a data-based Quick Look preview extension.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLPreviewReply
```

#### Overview

Create an instance of [`QLPreviewReply`](qlpreviewreply.md) from the method [`providePreview(for:completionHandler:)`](qlpreviewingcontroller/providepreview(for:completionhandler:).md) in your subclass of [`QLPreviewProvider`](qlpreviewprovider.md). Create an instance to return data; for example, an image, PDF, or HTML; that the system displays as the preview for the content that the system indicates with [`QLFilePreviewRequest`](qlfilepreviewrequest.md).

## Topics

### Creating a preview reply
- [init(fileURL: URL)](qlpreviewreply/init(fileurl:).md)
  Creates a preview reply from an existing file URL.
### Create a PDF preview reply
- [convenience init(forPDFWithPageSize: CGSize, createDocumentUsing: (QLPreviewReply) throws -> PDFDocument)](qlpreviewreply/init(forpdfwithpagesize:createdocumentusing:).md)
### Generating a preview reply
- [convenience init(dataOfContentType: UTType, contentSize: CGSize, createDataUsing: (QLPreviewReply) throws -> Data)](qlpreviewreply/init(dataofcontenttype:contentsize:createdatausing:).md)
### Drawing a preview reply
- [convenience init(contextSize: CGSize, isBitmap: Bool, drawUsing: (CGContext, QLPreviewReply) throws -> Void)](qlpreviewreply/init(contextsize:isbitmap:drawusing:).md)
### Inspecting a preview reply
- [var title: String](qlpreviewreply/title.md)
  The title for the system to display with the preview.
- [var attachments: [String : QLPreviewReplyAttachment]](qlpreviewreply/attachments.md)
  The attachments for a preview reply that provide additional data for the system to display the preview.
- [var stringEncoding: String.Encoding](qlpreviewreply/stringencoding-8ahm8.md)

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
- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
  A Quick Look preview request that indicates the content to preview.
- [class QLPreviewReplyAttachment](qlpreviewreplyattachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreply)*