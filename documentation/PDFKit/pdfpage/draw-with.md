# draw(with:)

**Framework**: PDFKit  
**Kind**: method

Draws the page within the specified box.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func draw(with box: PDFDisplayBox)
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

#### Discussion

This method takes into account the page rotation and draws clipped to the specified box. If the page is set to display annotations, this method also draws them. This method does not clear the background. To clear the background before drawing, use doc://com.apple.documentation/documentation/appkit/1473652-nsrectfill with `NSColor` set (typically) to white.

## See Also

- [var displaysAnnotations: Bool](pdfpage/displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func transformContext(for: PDFDisplayBox)](pdfpage/transformcontext(for:).md)
  Transforms the current context, given the specified box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/draw(with:))*