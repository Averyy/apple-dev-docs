# displaysAnnotations

**Framework**: PDFKit  
**Kind**: property

Returns a Boolean value indicating whether annotations are displayed for the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var displaysAnnotations: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the page will draw annotations when a drawing method is called.

## See Also

- [func draw(with: PDFDisplayBox)](pdfpage/draw(with:).md)
  Draws the page within the specified box.
- [var annotations: [PDFAnnotation]](pdfpage/annotations.md)
  Returns an array containing the page’s annotations.
- [func addAnnotation(PDFAnnotation)](pdfpage/addannotation(_:).md)
  Adds the specified annotation object to the page.
- [func removeAnnotation(PDFAnnotation)](pdfpage/removeannotation(_:).md)
  Removes the specified annotation from the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](pdfpage/annotation(at:).md)
  Returns the annotation, if there is one, at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/displaysannotations)*