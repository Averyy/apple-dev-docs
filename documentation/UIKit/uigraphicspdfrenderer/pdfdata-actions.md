# pdfData(actions:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) object that contains the encoded PDF.

#### Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting PDF encoded in a [`Data`](https://developer.apple.com/documentation/Foundation/Data) object.

You can call this method repeatedly to create multiple PDFs, each of which has identical dimensions and format.

## Parameters

- `actions`: A   block that, when invoked by the renderer, executes a set of drawing instructions to create the output PDF.

## See Also

- [func writePDF(to: URL, withActions: (UIGraphicsPDFRendererContext) -> Void) throws](uigraphicspdfrenderer/writepdf(to:withactions:).md)
  Creates a PDF from a set of drawing instructions and saves it to a specified URL.
- [UIGraphicsPDFRenderer.DrawingActions](uigraphicspdfrenderer/drawingactions.md)
  A closure for drawing PDF content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/pdfdata(actions:))*