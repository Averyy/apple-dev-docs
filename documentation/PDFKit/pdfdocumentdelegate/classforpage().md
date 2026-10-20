# classForPage()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns a `PDFPage` subclass for a page object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func classForPage() -> AnyClass
```

```objc
- (Class) classForPage;
```

## Mentions

- [Adding Custom Graphics to a PDF](../adding-custom-graphics-to-a-pdf.md)

## See Also

### Wrapping Document Elements
- [func `class`(forAnnotationClass: AnyClass) -> AnyClass](./class%28forannotationclass%29.md)
  Returns a `PDFAnnotation` subclass for a class.
- [func `class`(forAnnotationType: String) -> AnyClass](./class%28forannotationtype%29.md)
  Returns a `PDFAnnotation` subclass for an annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/classforpage())*