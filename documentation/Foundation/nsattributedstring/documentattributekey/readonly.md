# readOnly

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An indication of whether the document is read-only.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let readOnly: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object that contains an integer. A value of `1` indicates read-only. If the value is `0`, missing, or negative, the document doesn’t display as read-only.

This attribute is not related to the file system protection on the file. Instead, this attribute can affect how the file displays to the user.

The string constant in macOS 10.3 and earlier is `@"ReadOnly"`.

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
- [static let converted: NSAttributedString.DocumentAttributeKey](./converted.md)
  A value that indicates whether a filter service converted the file.
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
- [static let subject: NSAttributedString.DocumentAttributeKey](./subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](./title.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/readonly)*