# annotation(at:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the annotation, if there is one, at the specified point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func annotation(at point: CGPoint) -> PDFAnnotation?
```

*macOS*

```swift
func annotation(at point: NSPoint) -> PDFAnnotation?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFAnnotation *) annotationAtPoint:(CGPoint) point;
```

*macOS*

```objc
- (PDFAnnotation *) annotationAtPoint:(NSPoint) point;
```

## Discussion

Use this method for hit-testing based on the current cursor position. If more than one annotation shares the specified point, the frontmost (or topmost) one is returned (the annotations are searched in reverse order of their appearance in the PDF data file). Returns `NULL` if there is no annotation at `point`.

Specify the point in page space. Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Working with Annotations
- [var annotations: [PDFAnnotation]](./annotations.md)
  Returns an array containing the page’s annotations.
- [var displaysAnnotations: Bool](./displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func addAnnotation(PDFAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation object to the page.
- [func removeAnnotation(PDFAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation from the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/annotation(at:))*