# page

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the page that the destination refers to.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var page: PDFPage? { get }
```

```objc
@property (nonatomic, weak, readonly) PDFPage * page;
```

#### Return Value

The page referred to by the destination.

## See Also

### Getting Pages and Points
- [var point: CGPoint](./point.md)
  Returns the point, in page space, that the destination refers to.
- [let kPDFDestinationUnspecifiedValue: CGFloat](../kpdfdestinationunspecifiedvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdestination/page)*