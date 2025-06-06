# drawContentForPage(at:in:)

**Framework**: UIKit  
**Kind**: method

Draws the content of a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drawContentForPage(at pageIndex: Int, in contentRect: CGRect)
```

#### Discussion

The default implementation of this method does nothing. Override this method to draw the content of the specified page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md).

## Parameters

- `pageIndex`: The index of the page on which to draw content.
- `contentRect`: The area in which to draw content, in the coordinate system of the printable rectangle. This area is equal to   minus   and  .

## See Also

- [func drawPage(at: Int, in: CGRect)](uiprintpagerenderer/drawpage(at:in:).md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawheaderforpage(at:in:).md)
  Draws the header of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](uiprintpagerenderer/drawprintformatter(_:forpageat:).md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [func drawFooterForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawfooterforpage(at:in:).md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawcontentforpage(at:in:))*