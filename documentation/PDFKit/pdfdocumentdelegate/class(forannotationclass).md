# class(forAnnotationClass:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns a `PDFAnnotation` subclass for a class.

**Availability**:
- macOS 10.6+ - Deprecated in 10.12

## Declaration

```swift
optional func `class`(forAnnotationClass annotationClass: AnyClass) -> AnyClass
```

```objc
- (Class) classForAnnotationClass:(Class) annotationClass;
```

## See Also

### Wrapping Document Elements
- [func classForPage() -> AnyClass](./classforpage%28%29.md)
  Returns a `PDFPage` subclass for a page object.
- [func `class`(forAnnotationType: String) -> AnyClass](./class%28forannotationtype%29.md)
  Returns a `PDFAnnotation` subclass for an annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentdelegate/class(forannotationclass:))*