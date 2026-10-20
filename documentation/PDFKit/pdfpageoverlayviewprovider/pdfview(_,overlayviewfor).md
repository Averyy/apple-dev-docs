# pdfView(_:overlayViewFor:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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
func pdfView(_ view: PDFView, overlayViewFor page: PDFPage) -> UIView?
```

*macOS*

```swift
func pdfView(_ view: PDFView, overlayViewFor page: PDFPage) -> NSView?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (UIView *) pdfView:(PDFView *) view overlayViewForPage:(PDFPage *) page;
```

*macOS*

```objc
- (NSView *) pdfView:(PDFView *) view overlayViewForPage:(PDFPage *) page;
```

## See Also

### Instance Methods
- [func pdfView(PDFView, willDisplayOverlayView: UIView, for: PDFPage)](./pdfview%28_,willdisplayoverlayview,for%29.md)
- [func pdfView(PDFView, willEndDisplayingOverlayView: UIView, for: PDFPage)](./pdfview%28_,willenddisplayingoverlayview,for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpageoverlayviewprovider/pdfview(_:overlayviewfor:))*