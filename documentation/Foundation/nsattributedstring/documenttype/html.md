# html

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Hypertext markup language (HTML) document.

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
static let html: NSAttributedString.DocumentType
```

#### Discussion

> **Note**:  Apple discourages using this document type with the synchronous `initWithHTML:` initializers, which parse HTML in-process. Use the WebKit-based [`loadFromHTML(request:options:completionHandler:)`](../loadfromhtml%28request,options,completionhandler%29.md) family of methods instead, which parse HTML out-of-process for improved security, stability, and code isolation.

## See Also

### Getting keys for document types
- [static let docFormat: NSAttributedString.DocumentType](./docformat.md)
  Microsoft Word document.
- [static let macSimpleText: NSAttributedString.DocumentType](./macsimpletext.md)
  Macintosh SimpleText document.
- [static let officeOpenXML: NSAttributedString.DocumentType](./officeopenxml.md)
  ECMA Office Open XML text document format.
- [static let openDocument: NSAttributedString.DocumentType](./opendocument.md)
  OASIS Open Document text document format.
- [static let plain: NSAttributedString.DocumentType](./plain.md)
  Plain text document.
- [static let rtf: NSAttributedString.DocumentType](./rtf.md)
  Rich text format document.
- [static let rtfd: NSAttributedString.DocumentType](./rtfd.md)
  Rich text format with attachments document.
- [static let webArchive: NSAttributedString.DocumentType](./webarchive.md)
  WebKit WebArchive document.
- [static let wordML: NSAttributedString.DocumentType](./wordml.md)
  Microsoft Word XML (WordML schema) document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documenttype/html)*