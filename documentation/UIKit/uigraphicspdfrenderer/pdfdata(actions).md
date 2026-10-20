# pdfData(actions:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a PDF from a set of drawing instructions and returns it as a data object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func pdfData(actions: (UIGraphicsPDFRendererContext) -> Void) -> Data
```

```objc
- (NSData *) PDFDataWithActions:(UIGraphicsPDFDrawingActions) actions;
```

#### Return Value

A [`Data`](../../Foundation/data.md) object that contains the encoded PDF.

#### Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting PDF encoded in a [`Data`](../../Foundation/data.md) object.

You can call this method repeatedly to create multiple PDFs, each of which has identical dimensions and format.

## Parameters

- `actions`: A [`UIGraphicsPDFRenderer.DrawingActions`](./drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output PDF.

## See Also

### Managing the PDF data
- [func writePDF(to: URL, withActions: (UIGraphicsPDFRendererContext) -> Void) throws](./writepdf%28to,withactions%29.md)
  Creates a PDF from a set of drawing instructions and saves it to a specified URL.
- [UIGraphicsPDFRenderer.DrawingActions](./drawingactions.md)
  A closure for drawing PDF content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/pdfdata(actions:))*