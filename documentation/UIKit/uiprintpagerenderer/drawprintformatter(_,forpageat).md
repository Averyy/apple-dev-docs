# drawPrintFormatter(_:forPageAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) drawPrintFormatter:(UIPrintFormatter *) printFormatter forPageAtIndex:(NSInteger) pageIndex;
```

#### Discussion

The system invokes this method for each print formatter associated with the specified page. The default implementation invokes the [`draw(in:forPageAt:)`](../uiprintformatter/draw%28in,forpageat%29.md) method of each [`UIPrintFormatter`](../uiprintformatter.md) object.

Override this method to intermix custom drawing with the formatter drawing — for example, by adding an overlay or underlay graphic. Call [`draw(in:forPageAt:)`](../uiprintformatter/draw%28in,forpageat%29.md) to have the print formatter draw its portion of the page.

The system configures this method for drawing to the current graphics context according to [`UIGraphicsGetCurrentContext()`](../uigraphicsgetcurrentcontext%28%29.md).

## Parameters

- `printFormatter`: A [`UIPrintFormatter`](../uiprintformatter.md) object associated with the page at `pageIndex`.
- `pageIndex`: The index of the page for `printFormatter` to draw on.

## See Also

### Drawing a page
- [func drawPage(at: Int, in: CGRect)](./drawpage%28at,in%29.md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](./drawheaderforpage%28at,in%29.md)
  Draws the header of a page.
- [func drawContentForPage(at: Int, in: CGRect)](./drawcontentforpage%28at,in%29.md)
  Draws the content of a page.
- [func drawFooterForPage(at: Int, in: CGRect)](./drawfooterforpage%28at,in%29.md)
  Draws the footer of a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawprintformatter(_:forpageat:))*