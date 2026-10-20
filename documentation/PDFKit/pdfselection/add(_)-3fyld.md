# add(_:)

**Framework**: PDFKit  
**Kind**: method

Adds the specified array of selections to the receiving selection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ selections: [PDFSelection])
```

#### Discussion

This method provides better performance than multiple calls to `addSelection` if you need to add several selections to an existing selection. This is because the normalization of the selection (the removal of any overlaps between selections) occurs only once, after all selections have been added.

## See Also

- [class PDFSelection](pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.
- [func add(PDFSelection)](pdfselection/add(_:)-8c2r.md)
  Adds the specified selection to the receiving selection.
- [func extend(atEnd: Int)](pdfselection/extend(atend:).md)
  Extends the selection from its end toward the end of the document.
- [func extend(atStart: Int)](pdfselection/extend(atstart:).md)
  Extends the selection from its start toward the beginning of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/add(_:)-3fyld)*