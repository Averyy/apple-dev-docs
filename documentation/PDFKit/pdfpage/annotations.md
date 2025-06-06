# annotations

**Framework**: PDFKit  
**Kind**: property

Returns an array containing the page’s annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var annotations: [PDFAnnotation] { get }
```

#### Discussion

The elements of the array will most likely be typed to subclasses of the [`PDFAnnotation`](pdfannotation.md) class.

## See Also

- [var displaysAnnotations: Bool](pdfpage/displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func addAnnotation(PDFAnnotation)](pdfpage/addannotation(_:).md)
  Adds the specified annotation object to the page.
- [func removeAnnotation(PDFAnnotation)](pdfpage/removeannotation(_:).md)
  Removes the specified annotation from the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](pdfpage/annotation(at:).md)
  Returns the annotation, if there is one, at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/annotations)*