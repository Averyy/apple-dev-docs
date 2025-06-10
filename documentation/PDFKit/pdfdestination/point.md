# point

**Framework**: PDFKit  
**Kind**: property

Returns the point, in page space, that the destination refers to.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var point: NSPoint { get }
```

#### Return Value

The point, in page space, referred to by the destination.

#### Discussion

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [var page: PDFPage?](pdfdestination/page.md)
  Returns the page that the destination refers to.
- [let kPDFDestinationUnspecifiedValue: CGFloat](kpdfdestinationunspecifiedvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdestination/point)*