# drawFooterForPage(at:in:)

**Framework**: UIKit  
**Kind**: method

Draws the footer of a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drawFooterForPage(at pageIndex: Int, in footerRect: CGRect)
```

#### Discussion

The default implementation of this method does nothing. The system doesn’t call this method if [`footerHeight`](uiprintpagerenderer/footerheight.md) isn’t a positive value. Override this method to draw the footer of the specified page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md).

## Parameters

- `pageIndex`: The index of the page on which to draw the footer content.
- `footerRect`: The rectangle in which to draw the footer content. This rectangle uses the coordinate system of the paper rectangle ( ), with the origin of the coordinates at the top-left corner of the sheet.

## See Also

- [func drawPage(at: Int, in: CGRect)](uiprintpagerenderer/drawpage(at:in:).md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawheaderforpage(at:in:).md)
  Draws the header of a page.
- [func drawContentForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawcontentforpage(at:in:).md)
  Draws the content of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](uiprintpagerenderer/drawprintformatter(_:forpageat:).md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawfooterforpage(at:in:))*