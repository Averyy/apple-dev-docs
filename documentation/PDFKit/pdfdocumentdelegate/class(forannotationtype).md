# class(forAnnotationType:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns a `PDFAnnotation` subclass for an annotation type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func `class`(forAnnotationType annotationType: String) -> AnyClass
```

```objc
- (Class) classForAnnotationType:(NSString *) annotationType;
```

## Mentions

- [Adding Custom Graphics to a PDF](../adding-custom-graphics-to-a-pdf.md)

## See Also

### Wrapping Document Elements
- [func classForPage() -> AnyClass](./classforpage%28%29.md)
  Returns a `PDFPage` subclass for a page object.
- [func `class`(forAnnotationClass: AnyClass) -> AnyClass](./class%28forannotationclass%29.md)
  Returns a `PDFAnnotation` subclass for a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/class(forannotationtype:))*