# init(bounds:forType:withProperties:)

**Framework**: PDFKit  
**Kind**: init  
**Role**: Initializer

Creates a PDF annotation with the specified bounds, type, and optional properties.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
init(bounds: CGRect, forType annotationType: PDFAnnotationSubtype, withProperties properties: [AnyHashable : Any]?)
```

*macOS*

```swift
init(bounds: NSRect, forType annotationType: PDFAnnotationSubtype, withProperties properties: [AnyHashable : Any]?)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (instancetype) initWithBounds:(CGRect) bounds forType:(PDFAnnotationSubtype) annotationType withProperties:(NSDictionary *) properties;
```

*macOS*

```objc
- (instancetype) initWithBounds:(NSRect) bounds forType:(PDFAnnotationSubtype) annotationType withProperties:(NSDictionary *) properties;
```

## Parameters

- `bounds`: The bounding box of the annotation, in page-space coordinates.
- `annotationType`: The subtype of the annotation, such as text, link, or line.
- `properties`: A dictionary that contains properties of the annotation.

## See Also

### Creating an Annotation
- [struct PDFAnnotationSubtype](../pdfannotationsubtype.md)
  The type of annotation, such as circle, text, or ink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/init(bounds:fortype:withproperties:))*