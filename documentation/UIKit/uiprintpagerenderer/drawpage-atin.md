# drawPage(at:in:)

**Framework**: UIKit  
**Kind**: method

Draws a page of content for the printer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drawPage(at pageIndex: Int, in printableRect: CGRect)
```

#### Discussion

The default implementation of this method calls, in sequence, [`drawHeaderForPage(at:in:)`](uiprintpagerenderer/drawheaderforpage(at:in:).md), [`drawContentForPage(at:in:)`](uiprintpagerenderer/drawcontentforpage(at:in:).md), [`drawPrintFormatter(_:forPageAt:)`](uiprintpagerenderer/drawprintformatter(_:forpageat:).md), and [`drawFooterForPage(at:in:)`](uiprintpagerenderer/drawfooterforpage(at:in:).md). Override this method to draw the specified page of content for the printer.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md).

## Parameters

- `pageIndex`: The index of the page to draw.
- `printableRect`: The rectangle in which to draw printable content.

## See Also

- [func drawHeaderForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawheaderforpage(at:in:).md)
  Draws the header of a page.
- [func drawContentForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawcontentforpage(at:in:).md)
  Draws the content of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](uiprintpagerenderer/drawprintformatter(_:forpageat:).md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [func drawFooterForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawfooterforpage(at:in:).md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawpage(at:in:))*