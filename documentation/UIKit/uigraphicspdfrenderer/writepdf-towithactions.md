# writePDF(to:withActions:)

**Framework**: UIKit  
**Kind**: method

Creates a PDF from a set of drawing instructions and saves it to a specified URL.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func writePDF(to url: URL, withActions actions: (UIGraphicsPDFRendererContext) -> Void) throws
```

#### Discussion

You provide a set of drawing instructions as the block argument to this method, and the method attempts to write the resulting PDF to the supplied URL.

You can call this method repeatedly to create multiple PDFs, each of which has identical dimensions and format.

## Parameters

- `url`: The URL where the complete PDF file is saved.
- `actions`: A   closure that, when invoked by the renderer, executes a set of drawing instructions to create the output PDF.

## See Also

- [func pdfData(actions: (UIGraphicsPDFRendererContext) -> Void) -> Data](uigraphicspdfrenderer/pdfdata(actions:).md)
  Creates a PDF from a set of drawing instructions and returns it as a data object.
- [UIGraphicsPDFRenderer.DrawingActions](uigraphicspdfrenderer/drawingactions.md)
  A closure for drawing PDF content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/writepdf(to:withactions:))*