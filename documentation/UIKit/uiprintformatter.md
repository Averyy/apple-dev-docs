# UIPrintFormatter

**Framework**: UIKit  
**Kind**: class

An abstract base class for print formatters, which are objects that lay out custom printable content that can cross page boundaries.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrintFormatter
```

#### Overview

Given a print formatter, the printing system can automate the printing of the type of content associated with the print formatter. Examples of such content could be a web view, a mix of images and text, or a long text document. The UIKit framework provides several concrete subclasses of [`UIPrintFormatter`](uiprintformatter.md): [`UISimpleTextPrintFormatter`](uisimpletextprintformatter.md), [`UIMarkupTextPrintFormatter`](uimarkuptextprintformatter.md), and [`UIViewPrintFormatter`](uiviewprintformatter.md).

You can assign a single print formatter for a print job using the [`printFormatter`](uiprintinteractioncontroller/printformatter.md) property of the [`UIPrintInteractionController`](uiprintinteractioncontroller.md) shared instance; or you can specify one or more print formatters that are associated with specific pages of a page renderer through the [`addPrintFormatter(_:startingAtPageAt:)`](uiprintpagerenderer/addprintformatter(_:startingatpageat:).md)method of [`UIPrintPageRenderer`](uiprintpagerenderer.md). A page renderer is an instance of a custom subclass of [`UIPrintPageRenderer`](uiprintpagerenderer.md) that draws content for printing.

[`UIPrintFormatter`](uiprintformatter.md) publishes an interface that allows you to specify the starting page for a print job and the margins around the printed content; given that information plus the content, a print formatter computes the number of pages for the print job. The following image depicts the print-formatter properties, along with certain [`UIPrintPaper`](uiprintpaper.md) and [`UIPrintPageRenderer`](uiprintpagerenderer.md) properties, that define the layout of a multipage print job.

![Diagram that shows the layout of printed content.](https://docs-assets.developer.apple.com/published/5af87d7015f12142813615b85252c418/media-1965769.jpg)

Third-party subclasses of [`UIPrintFormatter`](uiprintformatter.md) aren’t recommended. If you have custom content to print, use a custom [`UIPrintPageRenderer`](uiprintpagerenderer.md) object.

## Topics

### Laying out the content
- [var perPageContentInsets: UIEdgeInsets](uiprintformatter/perpagecontentinsets.md)
  The margins for each printed page.
- [var maximumContentHeight: CGFloat](uiprintformatter/maximumcontentheight.md)
  The maximum height of the content area.
- [var maximumContentWidth: CGFloat](uiprintformatter/maximumcontentwidth.md)
  The maximum width of the content area.
- [var contentInsets: UIEdgeInsets](uiprintformatter/contentinsets.md)
  The distances the edges of content are inset from the printing rectangle.
### Managing pagination
- [var startPage: Int](uiprintformatter/startpage.md)
  The index of the first page that the print formatter lays out.
- [var pageCount: Int](uiprintformatter/pagecount.md)
  The number of pages to print.
### Drawing the content
- [func draw(in: CGRect, forPageAt: Int)](uiprintformatter/draw(in:forpageat:).md)
  Draws the portion of a print formatter’s content for the specified area of the specified page.
- [func rectForPage(at: Int) -> CGRect](uiprintformatter/rectforpage(at:).md)
  Returns the area that encloses a specified page of content.
### Communicating with the page renderer
- [func removeFromPrintPageRenderer()](uiprintformatter/removefromprintpagerenderer.md)
  Removes the print formatter from the page renderer.
- [var printPageRenderer: UIPrintPageRenderer?](uiprintformatter/printpagerenderer.md)
  Returns the page renderer for the print formatter.
### Requiring operations to take place on the main thread
- [var requiresMainThread: Bool](uiprintformatter/requiresmainthread.md)
  A Boolean value that determines whether the system executes the print formatter’s rendering operations on the main thread.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIMarkupTextPrintFormatter](uimarkuptextprintformatter.md)
- [UISimpleTextPrintFormatter](uisimpletextprintformatter.md)
- [UIViewPrintFormatter](uiviewprintformatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIViewPrintFormatter](uiviewprintformatter.md)
  An object that lays out the drawn content of a view for printing.
- [class UISimpleTextPrintFormatter](uisimpletextprintformatter.md)
  An object that lays out plain text for printing, possibly over multiple pages.
- [class UIMarkupTextPrintFormatter](uimarkuptextprintformatter.md)
  An object that lays out HTML text for a multipage print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter)*