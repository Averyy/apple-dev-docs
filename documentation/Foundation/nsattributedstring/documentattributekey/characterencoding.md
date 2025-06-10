# characterEncoding

**Framework**: Foundation  
**Kind**: property

The string encoding for the document.

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
static let characterEncoding: NSAttributedString.DocumentAttributeKey
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing integer specifying [`NSStringEncoding`](nsstringencoding.md) for the file; default for plain text is the default encoding. This key in options can specify the string encoding for reading the data. Upon return, the document attributes can contain the actual encoding used. For writing methods, this value is used for generating the plain text data.

The string constant in macOS 10.3 and earlier is `@"CharacterEncoding"`.

## See Also

- [static let author: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/author.md)
  The author of the document.
- [static let category: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/category.md)
  The document’s category.
- [static let comment: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/comment.md)
  The document comments.
- [static let company: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/company.md)
  The company or organization name associated with the document.
- [static let converted: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/converted.md)
  A value that indicates whether a filter service converted the file.
- [static let copyright: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/copyright.md)
  The document’s copyright information.
- [static let creationTime: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/creationtime.md)
  The creation date of the document.
- [static let editor: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/editor.md)
  The name of person who last edited the document.
- [static let keywords: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/keywords.md)
  The document keywords.
- [static let manager: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/manager.md)
  The name of the author’s manager.
- [static let modificationTime: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/modificationtime.md)
  The modification date of the document.
- [static let readOnly: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/readonly.md)
  An indication of whether the document is read-only.
- [static let subject: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/title.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/characterencoding)*