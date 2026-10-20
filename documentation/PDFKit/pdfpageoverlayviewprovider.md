# PDFPageOverlayViewProvider

**Framework**: PDFKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol PDFPageOverlayViewProvider : NSObjectProtocol
```

```objc
@protocol PDFPageOverlayViewProvider <NSObject>
```

## Topics

### Instance Methods
- [func pdfView(PDFView, overlayViewFor: PDFPage) -> UIView?](./pdfpageoverlayviewprovider/pdfview%28_,overlayviewfor%29.md)
- [func pdfView(PDFView, willDisplayOverlayView: UIView, for: PDFPage)](./pdfpageoverlayviewprovider/pdfview%28_,willdisplayoverlayview,for%29.md)
- [func pdfView(PDFView, willEndDisplayingOverlayView: UIView, for: PDFPage)](./pdfpageoverlayviewprovider/pdfview%28_,willenddisplayingoverlayview,for%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpageoverlayviewprovider)*