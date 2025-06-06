# add(_:)

**Framework**: PDFKit  
**Kind**: method

Adds the specified selection to the receiving selection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ selection: PDFSelection)
```

#### Discussion

Selections do not have to be contiguous. If the selection to be added overlaps with the receiving selection, the overlap is removed in a process called normalization.

## See Also

- [func add([PDFSelection])](pdfselection/add(_:)-3fyld.md)
  Adds the specified array of selections to the receiving selection.
- [func extend(atEnd: Int)](pdfselection/extend(atend:).md)
  Extends the selection from its end toward the end of the document.
- [func extend(atStart: Int)](pdfselection/extend(atstart:).md)
  Extends the selection from its start toward the beginning of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/add(_:)-8c2r)*