# QLPreviewReply

**Framework**: Quick Look  
**Kind**: class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class QLPreviewReply
```

#### Overview

To provide a data-based preview, you have to return a QLPreviewReply object.

## Topics

### Initializers
- [convenience init(contextSize: CGSize, isBitmap: Bool, drawUsing: (CGContext, QLPreviewReply) throws -> Void)](qlpreviewreply/init(contextsize:isbitmap:drawusing:).md)
- [convenience init(dataOfContentType: UTType, contentSize: CGSize, createDataUsing: (QLPreviewReply) throws -> Data)](qlpreviewreply/init(dataofcontenttype:contentsize:createdatausing:).md)
- [init(fileURL: URL)](qlpreviewreply/init(fileurl:).md)
- [convenience init(forPDFWithPageSize: CGSize, createDocumentUsing: (QLPreviewReply) throws -> PDFDocument)](qlpreviewreply/init(forpdfwithpagesize:createdocumentusing:).md)
### Instance Properties
- [var attachments: [String : QLPreviewReplyAttachment]](qlpreviewreply/attachments.md)
  Attachments for HTML data previews. The keys of the dictionary are the attachment identifiers (eg foo) that can be referenced with the cid:id URL (eg cid:foo).
- [var stringEncoding: String.Encoding](qlpreviewreply/stringencoding-8rrio.md)
- [var title: String](qlpreviewreply/title.md)
  Custom display title for the preview. If left as the empty string, QuickLook will use the file name.

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

- [class QLFilePreviewRequest](qlfilepreviewrequest.md)
- [class QLPreviewProvider](qlpreviewprovider.md)
- [class QLPreviewReplyAttachment](qlpreviewreplyattachment.md)
- [protocol QLPreviewItem](qlpreviewitem.md)
- [protocol QLPreviewingController](qlpreviewingcontroller.md)
  For view based previews, the view controller that implements the QLPreviewingController protocol must at least implement one of the two following methods: -[QLPreviewingController preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:], to generate previews for Spotlight searchable items. -[QLPreviewingController preparePreviewOfFileAtURL:completionHandler:], to generate previews for file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreply)*