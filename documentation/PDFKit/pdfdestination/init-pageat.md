# init(page:at:)

**Framework**: PDFKit  
**Kind**: init

Initializes the destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(page: PDFPage, at point: CGPoint)
```

#### Return Value

An initialized `PDFDestination` instance, or `NULL` if the object could not be initialized.

#### Discussion

Specify `point` in page space. Typically, there’s no need to initialize destinations. Instead, you get them from [`PDFAnnotationLink`](pdfannotationlink.md), [`PDFOutline`](pdfoutline.md), or [`PDFView`](pdfview.md) objects.

Page space is a 72-dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `page`: The page of the destination.
- `point`: The point of the destination, in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdestination/init(page:at:))*