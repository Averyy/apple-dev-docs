# QLPreviewReply

**Framework**: Quick Look UI  
**Kind**: class  
**Role**: Class

The class you create when providing a data-based Quick Look preview extension.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class QLPreviewReply
```

```objc
@interface QLPreviewReply : NSObject
```

#### Overview

Create an instance of [`QLPreviewReply`](./qlpreviewreply.md) from the method [`providePreview(for:completionHandler:)`](./qlpreviewingcontroller/providepreview%28for,completionhandler%29.md) in your subclass of [`QLPreviewProvider`](./qlpreviewprovider.md). Create an instance to return data, such as an image, PDF, or HTML, that the system displays as the preview for the content that [`QLFilePreviewRequest`](./qlfilepreviewrequest.md) specifies.

## Topics

### Creating a preview reply
- [init(fileURL: URL)](./qlpreviewreply/init%28fileurl%29.md)
  Creates a preview reply from an existing file URL.
### Creating a PDF preview reply
- [convenience init(forPDFWithPageSize: CGSize, createDocumentUsing: (QLPreviewReply) throws -> PDFDocument)](./qlpreviewreply/init%28forpdfwithpagesize,createdocumentusing%29.md)
### Generating a preview reply
- [convenience init(dataOfContentType: UTType, contentSize: CGSize, createDataUsing: (QLPreviewReply) throws -> Data)](./qlpreviewreply/init%28dataofcontenttype,contentsize,createdatausing%29.md)
### Drawing a preview reply
- [convenience init(contextSize: CGSize, isBitmap: Bool, drawUsing: (CGContext, QLPreviewReply) throws -> Void)](./qlpreviewreply/init%28contextsize,isbitmap,drawusing%29.md)
### Inspecting a preview reply
- [var title: String](./qlpreviewreply/title.md)
  The title for the system to display with the preview.
- [var attachments: [String : QLPreviewReplyAttachment]](./qlpreviewreply/attachments.md)
  The attachments for a preview reply that provide additional data for the system to display the preview.
- [var stringEncoding: String.Encoding](./qlpreviewreply/stringencoding-8ahm8.md)
### Instance Properties
- [stringEncoding](./qlpreviewreply/stringencoding-1k9kb.md)
  String encoding for text or html based previews. Defaults to NSUTF8StringEncoding.
### Instance Methods
- [- initForPDFWithPageSize:documentCreationBlock:](./qlpreviewreply/initforpdfwithpagesize_documentcreationblock_.md)
- [- initWithContextSize:isBitmap:drawingBlock:](./qlpreviewreply/initwithcontextsize_isbitmap_drawingblock_.md)
- [- initWithDataOfContentType:contentSize:dataCreationBlock:](./qlpreviewreply/initwithdataofcontenttype_contentsize_datacreationblock_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data-based Preview Extensions
- [class QLPreviewProvider](./qlpreviewprovider.md)
  A class that you subclass to provide a data-based Quick Look preview extension.
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
  A Quick Look preview request that indicates the content to preview.
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
  An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreply)*