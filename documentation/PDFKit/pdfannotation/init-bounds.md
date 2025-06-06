# init(bounds:)

**Framework**: PDFKit  
**Kind**: init

Creates a PDF annotation object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
convenience init(bounds: NSRect)
```

#### Return Value

An initialized `PDFAnnotation` instance, or `NULL` if the object can’t initialize.

#### Discussion

Subclasses of `PDFAnnotation` use this method to initialize annotation instances. Provide `bounds` in page-space coordinates. Invoking `initWithBounds:` directly on a `PDFAnnotation` object creates an illegal `NULL` type.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `bounds`: The bounding box of the annotation in page-space coordinates.

## See Also

- [convenience init(dictionary: [AnyHashable : Any], forPage: PDFPage?)](pdfannotation/init(dictionary:forpage:).md)
- [func removeAllAppearanceStreams()](pdfannotation/removeallappearancestreams.md)
- [func draw(with: PDFDisplayBox)](pdfannotation/draw(with:).md)
  Draws the annotation on its associated page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/init(bounds:))*