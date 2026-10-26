# QLPreviewReply

**Framework**: Quick Look  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewReply
```

```objc
@interface QLPreviewReply : NSObject
```

#### Overview

To provide a data-based preview, you have to return a QLPreviewReply object.

## Topics

### Initializers
- [convenience init(contextSize: CGSize, isBitmap: Bool, drawUsing: (CGContext, QLPreviewReply) throws -> Void)](./qlpreviewreply/init%28contextsize,isbitmap,drawusing%29.md)
- [convenience init(dataOfContentType: UTType, contentSize: CGSize, createDataUsing: (QLPreviewReply) throws -> Data)](./qlpreviewreply/init%28dataofcontenttype,contentsize,createdatausing%29.md)
- [init(fileURL: URL)](./qlpreviewreply/init%28fileurl%29.md)
- [convenience init(forPDFWithPageSize: CGSize, createDocumentUsing: (QLPreviewReply) throws -> PDFDocument)](./qlpreviewreply/init%28forpdfwithpagesize,createdocumentusing%29.md)
### Instance Properties
- [var attachments: [String : QLPreviewReplyAttachment]](./qlpreviewreply/attachments.md)
  Attachments for HTML data previews. The keys of the dictionary are the attachment identifiers (eg foo) that can be referenced with the cid:id URL (eg cid:foo).
- [var stringEncoding: String.Encoding](./qlpreviewreply/stringencoding-8rrio.md)
- [var title: String](./qlpreviewreply/title.md)
  Custom display title for the preview. If left as the empty string, QuickLook will use the file name.
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

### QuickLookUI symbols
- [class QLFilePreviewRequest](./qlfilepreviewrequest.md)
- [class QLPreviewProvider](./qlpreviewprovider.md)
- [class QLPreviewReplyAttachment](./qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](./qlpreviewitem.md)
- [protocol QLPreviewingController](./qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreply)*