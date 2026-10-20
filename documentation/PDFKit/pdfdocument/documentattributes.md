# documentAttributes

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of document metadata.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var documentAttributes: [AnyHashable : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary * documentAttributes;
```

#### Return Value

The dictionary of document metadata. The dictionary may be empty, or only some of the keys may have associated values.

#### Discussion

Metadata is optional for PDF documents.

## See Also

### Related Documentation
- [struct PDFDocumentAttribute](../pdfdocumentattribute.md)
  A structure that specifies document attributes.
### Accessing Document Information
- [var documentURL: URL?](./documenturl.md)
  The URL for the document.
- [var majorVersion: Int](./majorversion.md)
  The major version of the document.
- [var minorVersion: Int](./minorversion.md)
  The minor version of the document.
- [var string: String?](./string.md)
  A string representing the textual content for the entire document.
- [func outlineItem(for: PDFSelection) -> PDFOutline?](./outlineitem%28for%29.md)
  Returns the most likely parent PDF outline object for the selection.
- [var outlineRoot: PDFOutline?](./outlineroot.md)
  The document’s root outline to a PDF outline object.
- [var documentRef: CGPDFDocument?](./documentref.md)
  The `CGPDFDocument` associated with the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/documentattributes)*