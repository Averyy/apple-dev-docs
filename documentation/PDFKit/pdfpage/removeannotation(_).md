# removeAnnotation(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeAnnotation:(PDFAnnotation *) annotation;
```

## See Also

### Working with Annotations
- [var annotations: [PDFAnnotation]](./annotations.md)
  Returns an array containing the page’s annotations.
- [var displaysAnnotations: Bool](./displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func addAnnotation(PDFAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation object to the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](./annotation%28at%29.md)
  Returns the annotation, if there is one, at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/removeannotation(_:))*