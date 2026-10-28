# converted

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A value that indicates whether a filter service converted the file.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let converted: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object containing an integer. Indicates whether the file was converted by a filter service.

If missing or 0, the file was originally in the format specified by [`documentType`](./documenttype.md). If negative, the file was originally in the format specified by document type, but the conversion to [`NSAttributedString`](../../nsattributedstring.md) may have been lossy. If 1 or more, it was converted to this type by a filter service.

The string constant in macOS 10.3 and earlier is `@"Converted"`.

## See Also

### Getting document metadata keys
- [static let author: NSAttributedString.DocumentAttributeKey](./author.md)
  The author of the document.
- [static let category: NSAttributedString.DocumentAttributeKey](./category.md)
  The document’s category.
- [static let characterEncoding: NSAttributedString.DocumentAttributeKey](./characterencoding.md)
  The string encoding for the document.
- [static let cocoaVersionDocumentAttribute: NSAttributedString.DocumentAttributeKey](./cocoaversiondocumentattribute.md)
  The version of Cocoa that created the file.
- [static let comment: NSAttributedString.DocumentAttributeKey](./comment.md)
  The document comments.
- [static let company: NSAttributedString.DocumentAttributeKey](./company.md)
  The company or organization name associated with the document.
- [static let copyright: NSAttributedString.DocumentAttributeKey](./copyright.md)
  The document’s copyright information.
- [static let creationTime: NSAttributedString.DocumentAttributeKey](./creationtime.md)
  The creation date of the document.
- [static let editor: NSAttributedString.DocumentAttributeKey](./editor.md)
  The name of person who last edited the document.
- [static let keywords: NSAttributedString.DocumentAttributeKey](./keywords.md)
  The document keywords.
- [static let manager: NSAttributedString.DocumentAttributeKey](./manager.md)
  The name of the author’s manager.
- [static let modificationTime: NSAttributedString.DocumentAttributeKey](./modificationtime.md)
  The modification date of the document.
- [static let readOnly: NSAttributedString.DocumentAttributeKey](./readonly.md)
  An indication of whether the document is read-only.
- [static let subject: NSAttributedString.DocumentAttributeKey](./subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](./title.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/converted)*