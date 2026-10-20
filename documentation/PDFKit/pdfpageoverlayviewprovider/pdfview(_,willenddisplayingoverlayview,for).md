# pdfView(_:willEndDisplayingOverlayView:for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
optional func pdfView(_ pdfView: PDFView, willEndDisplayingOverlayView overlayView: UIView, for page: PDFPage)
```

*macOS*

```swift
optional func pdfView(_ pdfView: PDFView, willEndDisplayingOverlayView overlayView: NSView, for page: PDFPage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) pdfView:(PDFView *) pdfView willEndDisplayingOverlayView:(UIView *) overlayView forPage:(PDFPage *) page;
```

*macOS*

```objc
- (void) pdfView:(PDFView *) pdfView willEndDisplayingOverlayView:(NSView *) overlayView forPage:(PDFPage *) page;
```

## See Also

### Instance Methods
- [func pdfView(PDFView, overlayViewFor: PDFPage) -> UIView?](./pdfview%28_,overlayviewfor%29.md)
- [func pdfView(PDFView, willDisplayOverlayView: UIView, for: PDFPage)](./pdfview%28_,willdisplayoverlayview,for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpageoverlayviewprovider/pdfview(_:willenddisplayingoverlayview:for:))*