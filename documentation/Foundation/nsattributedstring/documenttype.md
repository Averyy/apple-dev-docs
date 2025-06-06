# NSAttributedString.DocumentType

**Framework**: Foundation  
**Kind**: struct

Constants for the document type document attribute key.

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
struct DocumentType
```

#### Overview

Use these constants as values for the [`documentType`](nsattributedstring/documentattributekey/documenttype.md) key in the document attributes dictionary.

## Topics

### Getting keys for document types
- [static let docFormat: NSAttributedString.DocumentType](nsattributedstring/documenttype/docformat.md)
  Microsoft Word document.
- [static let html: NSAttributedString.DocumentType](nsattributedstring/documenttype/html.md)
  Hypertext markup language (HTML) document.
- [static let macSimpleText: NSAttributedString.DocumentType](nsattributedstring/documenttype/macsimpletext.md)
  Macintosh SimpleText document.
- [static let officeOpenXML: NSAttributedString.DocumentType](nsattributedstring/documenttype/officeopenxml.md)
  ECMA Office Open XML text document format.
- [static let openDocument: NSAttributedString.DocumentType](nsattributedstring/documenttype/opendocument.md)
  OASIS Open Document text document format.
- [static let plain: NSAttributedString.DocumentType](nsattributedstring/documenttype/plain.md)
  Plain text document.
- [static let rtf: NSAttributedString.DocumentType](nsattributedstring/documenttype/rtf.md)
  Rich text format document.
- [static let rtfd: NSAttributedString.DocumentType](nsattributedstring/documenttype/rtfd.md)
  Rich text format with attachments document.
- [static let webArchive: NSAttributedString.DocumentType](nsattributedstring/documenttype/webarchive.md)
  WebKit WebArchive document.
- [static let wordML: NSAttributedString.DocumentType](nsattributedstring/documenttype/wordml.md)
  Microsoft Word XML (WordML schema) document.
### Initializers
- [init(String)](nsattributedstring/documenttype/init(_:).md)
  Creates a document type.
- [init(rawValue: String)](nsattributedstring/documenttype/init(rawvalue:).md)
  Creates a document type with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey.md)
  The attributes you apply to an entire document.
- [NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documenttype)*