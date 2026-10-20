# displaysAnnotations

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL displaysAnnotations;
```

#### Discussion

If [`true`](../../Swift/true.md), the page will draw annotations when a drawing method is called.

## See Also

### Related Documentation
- [func draw(with: PDFDisplayBox)](./draw%28with%29.md)
  Draws the page within the specified box.
### Working with Annotations
- [var annotations: [PDFAnnotation]](./annotations.md)
  Returns an array containing the page’s annotations.
- [func addAnnotation(PDFAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation object to the page.
- [func removeAnnotation(PDFAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation from the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](./annotation%28at%29.md)
  Returns the annotation, if there is one, at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/displaysannotations)*