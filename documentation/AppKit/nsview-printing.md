# Printing

**Framework**: AppKit  
**Role**: API Collection

Create a printable version of your view’s content and handle pagination and printer-related behaviors.

## Topics

### Printing the View’s Content
- [func printView(Any?)](./nsview/printview%28_%29.md)
  This action method opens the Print panel, and if the user chooses an option other than canceling, prints the view and all its subviews to the device specified in the Print panel.
- [func beginPage(in: NSRect, atPlacement: NSPoint)](./nsview/beginpage%28in,atplacement%29.md)
  Called at the beginning of each page, this method sets up the coordinate system so that a region inside the view’s bounds is translated to a specified location.
- [func dataWithEPS(inside: NSRect) -> Data](./nsview/datawitheps%28inside%29.md)
  Returns EPS data that draws the region of the view within a specified rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](./nsview/datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the view within a specified rectangle.
- [var printJobTitle: String](./nsview/printjobtitle.md)
  The view’s print job title.
- [var pageHeader: NSAttributedString](./nsview/pageheader.md)
  A default header string that includes the print job title and date.
- [var pageFooter: NSAttributedString](./nsview/pagefooter.md)
  A default footer string that includes the current page number and page count.
- [func writeEPS(inside: NSRect, to: NSPasteboard)](./nsview/writeeps%28inside,to%29.md)
  Writes EPS data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func writePDF(inside: NSRect, to: NSPasteboard)](./nsview/writepdf%28inside,to%29.md)
  Writes PDF data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func drawPageBorder(with: NSSize)](./nsview/drawpageborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each logical page.
- [func drawSheetBorder(with: NSSize)](./nsview/drawsheetborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each printed sheet.
### Handling Pagination
- [var heightAdjustLimit: CGFloat](./nsview/heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](./nsview/widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](./nsview/adjustpagewidthnew%28_,left,right,limit%29.md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](./nsview/adjustpageheightnew%28_,top,bottom,limit%29.md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](./nsview/knowspagerange%28_%29.md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](./nsview/rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](./nsview/locationofprintrect%28_%29.md)
  Invoked by [`printView(_:)`](./nsview/printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.
### Writing Conforming Rendering Instructions
- [func beginDocument()](./nsview/begindocument%28%29.md)
  Invoked at the beginning of the printing session, this method sets up the current graphics context.
- [func endDocument()](./nsview/enddocument%28%29.md)
  This method is invoked at the end of the printing session.
- [func endPage()](./nsview/endpage%28%29.md)
  Writes the end of a conforming page.

## See Also

### Managing the view’s content
- [Layout](./layout.md)
  Specify the size and position your view relative to other nearby views using rules that update your view hierarchy automatically.
- [Drawing](./nsview-drawing.md)
  Draw the content of custom views and update that content when the view’s size or appearance changes.
- [protocol NSViewContentSelectionInfo](./nsviewcontentselectioninfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview-printing)*