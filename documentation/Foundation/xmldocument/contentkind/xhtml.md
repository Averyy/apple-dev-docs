# XMLDocument.ContentKind.xhtml

**Framework**: Foundation  
**Kind**: case

The document output is XHTML.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case xhtml
```

#### Discussion

This is set automatically if the `NSXMLDocumentTidyHTML` option is set and NSXML detects HTML.

## See Also

- [XMLDocument.ContentKind.html](xmldocument/contentkind/html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](xmldocument/contentkind/text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.
- [XMLDocument.ContentKind.xml](xmldocument/contentkind/xml.md)
  The default type of document content type, which is XML.
- [XMLDocument.ContentKind.html](xmldocument/contentkind/html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](xmldocument/contentkind/text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.
- [XMLDocument.ContentKind.xml](xmldocument/contentkind/xml.md)
  The default type of document content type, which is XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/contentkind/xhtml)*