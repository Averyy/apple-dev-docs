# init(bounds:forType:withProperties:)

**Framework**: PDFKit  
**Kind**: init

Creates a PDF annotation with the specified bounds, type, and optional properties.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(bounds: CGRect, forType annotationType: PDFAnnotationSubtype, withProperties properties: [AnyHashable : Any]?)
```

## Parameters

- `bounds`: The bounding box of the annotation, in page-space coordinates.
- `annotationType`: The subtype of the annotation, such as text, link, or line.
- `properties`: A dictionary that contains properties of the annotation.

## See Also

- [struct PDFAnnotationSubtype](pdfannotationsubtype.md)
  The type of annotation, such as circle, text, or ink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/init(bounds:fortype:withproperties:))*