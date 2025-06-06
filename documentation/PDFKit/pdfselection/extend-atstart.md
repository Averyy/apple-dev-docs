# extend(atStart:)

**Framework**: PDFKit  
**Kind**: method

Extends the selection from its start toward the beginning of the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func extend(atStart precede: Int)
```

#### Discussion

The selection may be extended by any amount, up to and including the beginning of the document.

## See Also

- [func add(PDFSelection)](pdfselection/add(_:)-8c2r.md)
  Adds the specified selection to the receiving selection.
- [func add([PDFSelection])](pdfselection/add(_:)-3fyld.md)
  Adds the specified array of selections to the receiving selection.
- [func extend(atEnd: Int)](pdfselection/extend(atend:).md)
  Extends the selection from its end toward the end of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/extend(atstart:))*