# UIPrintPageRenderer

**Framework**: UIKit  
**Kind**: class

An object that draws pages of content to print, with or without the assistance of print formatters.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrintPageRenderer
```

#### Overview

A page renderer is an instance of a custom subclass of [`UIPrintPageRenderer`](uiprintpagerenderer.md). When you compose a print job using the shared instance of [`UIPrintInteractionController`](uiprintinteractioncontroller.md), you assign the page renderer to the [`printPageRenderer`](uiprintinteractioncontroller/printpagerenderer.md) property of that instance. The subclass typically overrides one or more of the five `draw...` methods.

The [`drawPage(at:in:)`](uiprintpagerenderer/drawpage(at:in:).md) by default calls each of the other draw methods, in the order listed below. Your app can override it if you want to have complete control over what to draw for printing.

- Override [`drawHeaderForPage(at:in:)`](uiprintpagerenderer/drawheaderforpage(at:in:).md) to draw content in the header.
- Override [`drawContentForPage(at:in:)`](uiprintpagerenderer/drawcontentforpage(at:in:).md) to draw the main content of the print job in the area between the header and the footer.
- Override [`drawPrintFormatter(_:forPageAt:)`](uiprintpagerenderer/drawprintformatter(_:forpageat:).md) to intermix custom drawing with the drawing that an associated print formatter performs. The system calls this method for each print formatter associated with a particular page.
- Override [`drawFooterForPage(at:in:)`](uiprintpagerenderer/drawfooterforpage(at:in:).md) to draw content in the footer.

[`UIPrintPageRenderer`](uiprintpagerenderer.md) usually requires you to specify the number of pages of printable content by overriding [`numberOfPages`](uiprintpagerenderer/numberofpages.md). It also allows you to specify the heights of page headers and footers.

You may assign one or more print formatters — [`UIPrintFormatter`](uiprintformatter.md) objects that can lay out printable content of a certain kind — to specific page ranges of the content. For example, if your printable content is partially HTML, you may assign an instance of the [`UIMarkupTextPrintFormatter`](uimarkuptextprintformatter.md) object to the starting page of HTML content. You assign a print formatter using the [`addPrintFormatter(_:startingAtPageAt:)`](uiprintpagerenderer/addprintformatter(_:startingatpageat:).md) method and you can get the print formatters for a particular page by calling [`printFormattersForPage(at:)`](uiprintpagerenderer/printformattersforpage(at:).md).

## Topics

### Accessing information about the print job
- [var numberOfPages: Int](uiprintpagerenderer/numberofpages.md)
  The number of pages to render.
- [var paperRect: CGRect](uiprintpagerenderer/paperrect.md)
  The size of the paper for printing.
- [var printableRect: CGRect](uiprintpagerenderer/printablerect.md)
  The area in which printing can occur.
### Specifying header and footer heights
- [var headerHeight: CGFloat](uiprintpagerenderer/headerheight.md)
  The height of the page header.
- [var footerHeight: CGFloat](uiprintpagerenderer/footerheight.md)
  The height of the page footer.
### Managing print formatters
- [func addPrintFormatter(UIPrintFormatter, startingAtPageAt: Int)](uiprintpagerenderer/addprintformatter(_:startingatpageat:).md)
  Adds a print formatter to the page renderer starting at the specified page.
- [func printFormattersForPage(at: Int) -> [UIPrintFormatter]?](uiprintpagerenderer/printformattersforpage(at:).md)
  Returns the print formatters for a specified page.
- [var printFormatters: [UIPrintFormatter]?](uiprintpagerenderer/printformatters.md)
  The print formatters for the page renderer.
### Preparing for drawing
- [func prepare(forDrawingPages: NSRange)](uiprintpagerenderer/prepare(fordrawingpages:).md)
  Prepares the renderer for drawing a range of pages.
### Drawing a page
- [func drawPage(at: Int, in: CGRect)](uiprintpagerenderer/drawpage(at:in:).md)
  Draws a page of content for the printer.
- [func drawHeaderForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawheaderforpage(at:in:).md)
  Draws the header of a page.
- [func drawContentForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawcontentforpage(at:in:).md)
  Draws the content of a page.
- [func drawPrintFormatter(UIPrintFormatter, forPageAt: Int)](uiprintpagerenderer/drawprintformatter(_:forpageat:).md)
  Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [func drawFooterForPage(at: Int, in: CGRect)](uiprintpagerenderer/drawfooterforpage(at:in:).md)
  Draws the footer of a page.
### Managing the rendering quality
- [func currentRenderingQuality(forRequested: UIPrintRenderingQuality) -> UIPrintRenderingQuality](uiprintpagerenderer/currentrenderingquality(forrequested:).md)
  Determines the actual print-rendering quality according to the requested rendering quality.
- [enum UIPrintRenderingQuality](uiprintrenderingquality.md)
  Constants that represent the rendering quality for a print operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md)
  Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer)*