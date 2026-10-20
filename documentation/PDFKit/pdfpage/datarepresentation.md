# dataRepresentation

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the PDF data (that is, a PDF document) representing this page. This method does not preserve external page links.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var dataRepresentation: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * dataRepresentation;
```

## See Also

### Instance Properties
- [var pageRef: CGPDFPage?](./pageref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/datarepresentation)*