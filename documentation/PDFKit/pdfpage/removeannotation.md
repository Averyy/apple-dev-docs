# removeAnnotation(_:)

**Framework**: PDFKit  
**Kind**: method

Removes the specified annotation from the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAnnotation(_ annotation: PDFAnnotation)
```

## See Also

- [var annotations: [PDFAnnotation]](pdfpage/annotations.md)
  Returns an array containing the page’s annotations.
- [var displaysAnnotations: Bool](pdfpage/displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func addAnnotation(PDFAnnotation)](pdfpage/addannotation(_:).md)
  Adds the specified annotation object to the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](pdfpage/annotation(at:).md)
  Returns the annotation, if there is one, at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/removeannotation(_:))*