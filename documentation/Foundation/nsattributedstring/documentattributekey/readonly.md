# readOnly

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object that contains an integer. A value of `1` indicates read-only. If the value is `0`, missing, or negative, the document doesn’t display as read-only.

This attribute is not related to the file system protection on the file. Instead, this attribute can affect how the file displays to the user.

The string constant in macOS 10.3 and earlier is `@"ReadOnly"`.

## See Also

- [static let author: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/author.md)
  The author of the document.
- [static let category: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/category.md)
  The document’s category.
- [static let characterEncoding: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/characterencoding.md)
  The string encoding for the document.
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
- [static let subject: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/title.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/readonly)*