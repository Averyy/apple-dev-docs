# outlineItem(for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the most likely parent PDF outline object for the selection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func outlineItem(for selection: PDFSelection) -> PDFOutline?
```

```objc
- (PDFOutline *) outlineItemForSelection:(PDFSelection *) selection;
```

#### Return Value

The PDF outline object that is the most likely parent of the specified selection. Note that only the point representing the first character of the selection is considered in this method.

#### Discussion

Typically, outlines represent structural items such as chapters. You can use this method to identify the chapter that a selection falls within.

## Parameters

- `selection`: The area of the document currently selected by the user. A selection can span multiple outline items, but only the point representing the first character is considered.

## See Also

### Accessing Document Information
- [var documentURL: URL?](./documenturl.md)
  The URL for the document.
- [var majorVersion: Int](./majorversion.md)
  The major version of the document.
- [var minorVersion: Int](./minorversion.md)
  The minor version of the document.
- [var string: String?](./string.md)
  A string representing the textual content for the entire document.
- [var outlineRoot: PDFOutline?](./outlineroot.md)
  The document’s root outline to a PDF outline object.
- [var documentAttributes: [AnyHashable : Any]?](./documentattributes.md)
  A dictionary of document metadata.
- [var documentRef: CGPDFDocument?](./documentref.md)
  The `CGPDFDocument` associated with the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/outlineitem(for:))*