# XMLDocument.ContentKind.xhtml

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The document output is XHTML.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case xhtml
```

```c
NSXMLDocumentXHTMLKind
```

#### Discussion

This is set automatically if the `NSXMLDocumentTidyHTML` option is set and NSXML detects HTML.

## See Also

### Enumeration Cases
- [XMLDocument.ContentKind.html](./html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](./text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.
- [XMLDocument.ContentKind.xml](./xml.md)
  The default type of document content type, which is XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/contentkind/xhtml)*