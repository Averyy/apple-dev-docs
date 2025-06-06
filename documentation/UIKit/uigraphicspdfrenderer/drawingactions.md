# UIGraphicsPDFRenderer.DrawingActions

**Framework**: UIKit  
**Kind**: typealias

A closure for drawing PDF content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias DrawingActions = (UIGraphicsPDFRendererContext) -> Void
```

#### Discussion

`UIGraphicsPDFDrawingActions` defines a block type that takes a [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the PDF drawing methods on [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md). Your block should use the provided PDF renderer context to perform the drawing operations you want the renderer to execute.

See [`Creating a PDF with a PDF renderer`](uigraphicspdfrenderer#Creating-a-PDF-with-a-PDF-renderer.md) for an example use of a `UIGraphicsPDFDrawingActions` block.

## See Also

- [func pdfData(actions: (UIGraphicsPDFRendererContext) -> Void) -> Data](uigraphicspdfrenderer/pdfdata(actions:).md)
  Creates a PDF from a set of drawing instructions and returns it as a data object.
- [func writePDF(to: URL, withActions: (UIGraphicsPDFRendererContext) -> Void) throws](uigraphicspdfrenderer/writepdf(to:withactions:).md)
  Creates a PDF from a set of drawing instructions and saves it to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/drawingactions)*