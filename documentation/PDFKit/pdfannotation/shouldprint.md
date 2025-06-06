# shouldPrint

**Framework**: PDFKit  
**Kind**: property

Returns a Boolean value indicating whether the annotation should appear when the document is printed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var shouldPrint: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the annotation should appear when the PDF document is printed; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

`PDFPage` respects this flag when printing.

## See Also

- [func draw(with: PDFDisplayBox, in: CGContext)](pdfannotation/draw(with:in:).md)
  Draws the annotation in a graphics context using page-space coordinates relative to the origin of the specified box.
- [var shouldDisplay: Bool](pdfannotation/shoulddisplay.md)
  Returns a Boolean value indicating whether the annotation should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/shouldprint)*