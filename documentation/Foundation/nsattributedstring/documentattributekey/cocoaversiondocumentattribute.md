# cocoaVersionDocumentAttribute

**Framework**: Foundation  
**Kind**: property

The version of Cocoa that created the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let cocoaVersion: NSAttributedString.DocumentAttributeKey
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing a float. For RTF files only, stores the version of Cocoa with which the file was created. Absence of this value indicates RTF file not created by Cocoa or its predecessors.

Values less than `100` are pre–macOS; `100` is macOS 10.0 or 10.1; `102` is macOS 10.2 and 10.3; values greater than `102` correspond to values of `NSAppKitVersionNumber` in macOS 10.4 and later.

The string constant in macOS 10.3 and earlier is `@"CocoaRTFVersion"`.

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
- [static let readOnly: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/readonly.md)
  An indication of whether the document is read-only.
- [static let subject: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/subject.md)
  The subject of the document.
- [static let title: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/title.md)
  The document title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/cocoaversiondocumentattribute)*