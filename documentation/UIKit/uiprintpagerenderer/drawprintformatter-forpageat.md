# drawPrintFormatter(_:forPageAt:)

**Framework**: UIKit  
**Kind**: method

Performs custom drawing in addition to the specified print formatter’s drawing for a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drawPrintFormatter(_ printFormatter: UIPrintFormatter, forPageAt pageIndex: Int)
```

#### Discussion

The system invokes this method for each print formatter associated with the specified page. The default implementation invokes the [`draw(in:forPageAt:)`](uiprintformatter/draw(in:forpageat:).md) method of each [`UIPrintFormatter`](uiprintformatter.md) object.

Override this method to intermix custom drawing with the formatter drawing — for example, by adding an overlay or underlay graphic. Call [`draw(in:forPageAt:)`](uiprintformatter/draw(in:forpageat:).md) to have the print formatter draw its portion of the page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md).

## Parameters

- `printFormatter`: A   object associated with the page at  .
- `pageIndex`: The index of the page for   to draw on.

## See Also

- [func drawPage(at: Int, in: CGRect)](uiprintpagerenderer/drawpage(at:in:).md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawheaderforpage(at:in:).md)
  Draws the header of a page.
- [func drawContentForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawcontentforpage(at:in:).md)
  Draws the content of a page.
- [func drawFooterForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawfooterforpage(at:in:).md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawprintformatter(_:forpageat:))*