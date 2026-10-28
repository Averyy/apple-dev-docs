# drawContentForPage(at:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws the content of a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drawContentForPage(at pageIndex: Int, in contentRect: CGRect)
```

```objc
- (void) drawContentForPageAtIndex:(NSInteger) pageIndex inRect:(CGRect) contentRect;
```

## Discussion

The default implementation of this method does nothing. Override this method to draw the content of the specified page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](../uigraphicsgetcurrentcontext%28%29.md).

## Parameters

- `pageIndex`: The index of the page on which to draw content.
- `contentRect`: The area in which to draw content, in the coordinate system of the printable rectangle. This area is equal to [`printableRect`](./printablerect.md) minus [`headerHeight`](./headerheight.md) and [`footerHeight`](./footerheight.md).

## See Also

### Drawing a page
- [func drawPage(at: Int, in: CGRect)](./drawpage%28at,in%29.md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](./drawheaderforpage%28at,in%29.md)
  Draws the header of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](./drawprintformatter%28_,forpageat%29.md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [func drawFooterForPage(at: Int, in: CGRect)](./drawfooterforpage%28at,in%29.md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawcontentforpage(at:in:))*