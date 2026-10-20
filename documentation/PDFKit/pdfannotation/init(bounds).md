# init(bounds:)

**Framework**: PDFKit  
**Kind**: init  
**Role**: Initializer

Creates a PDF annotation object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

> **Deprecated**: Use [`init(bounds:forType:withProperties:)`](./init%28bounds,fortype,withproperties%29.md) instead.

## Declaration

```swift
convenience init(bounds: NSRect)
```

```objc
- (instancetype) initWithBounds:(NSRect) bounds;
```

#### Return Value

An initialized `PDFAnnotation` instance, or `NULL` if the object can’t initialize.

#### Discussion

Subclasses of `PDFAnnotation` use this method to initialize annotation instances. Provide `bounds` in page-space coordinates. Invoking `initWithBounds:` directly on a `PDFAnnotation` object creates an illegal `NULL` type.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `bounds`: The bounding box of the annotation in page-space coordinates.

## See Also

### Deprecated Methods
- [convenience init(dictionary: [AnyHashable : Any], forPage: PDFPage?)](./init%28dictionary,forpage%29.md)
- [func removeAllAppearanceStreams()](./removeallappearancestreams%28%29.md)
- [func draw(with: PDFDisplayBox)](./draw%28with%29.md)
  Draws the annotation on its associated page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/init(bounds:))*