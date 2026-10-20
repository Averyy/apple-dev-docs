# delegate

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The object acting as the delegate for the `PDFDocument` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PDFDocumentDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PDFDocumentDelegate> delegate;
```

## See Also

### Setting the Delegate
- [protocol PDFDocumentDelegate](../pdfdocumentdelegate.md)
  The delegate for the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/delegate)*