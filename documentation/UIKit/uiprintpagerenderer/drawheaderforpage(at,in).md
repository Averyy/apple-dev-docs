# drawHeaderForPage(at:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws the header of a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drawHeaderForPage(at pageIndex: Int, in headerRect: CGRect)
```

```objc
- (void) drawHeaderForPageAtIndex:(NSInteger) pageIndex inRect:(CGRect) headerRect;
```

#### Discussion

The default implementation of this method does nothing. The system doesn’t call this method if [`headerHeight`](./headerheight.md) isn’t a positive value. Override this method to draw the header of the specified page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](../uigraphicsgetcurrentcontext%28%29.md).

## Parameters

- `pageIndex`: The index of the page on which to draw the header.
- `headerRect`: The rectangle in which to draw the header content. This rectangle uses the coordinate system of the paper rectangle ([`paperRect`](./paperrect.md)), with the origin of the coordinates at the top-left corner of the sheet.

## See Also

### Drawing a page
- [func drawPage(at: Int, in: CGRect)](./drawpage%28at,in%29.md)
  Draws a page of content for the printer.
- [func drawContentForPage(at: Int, in: CGRect)](./drawcontentforpage%28at,in%29.md)
  Draws the content of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](./drawprintformatter%28_,forpageat%29.md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [func drawFooterForPage(at: Int, in: CGRect)](./drawfooterforpage%28at,in%29.md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawheaderforpage(at:in:))*