# drawPageBorder(with:)

**Framework**: AppKit  
**Kind**: method

Allows applications that use the AppKit pagination facility to draw additional marks on each logical page.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawPageBorder(with borderSize: NSSize)
```

#### Discussion

The marks can be such things as alignment marks or a virtual sheet border of size `borderSize`. The default implementation doesn’t draw anything.

## Parameters

- `borderSize`: An   structure that defines a logical page.

## See Also

- [func printView(Any?)](nsview/printview(_:).md)
  This action method opens the Print panel, and if the user chooses an option other than canceling, prints the view and all its subviews to the device specified in the Print panel.
- [func beginPage(in: NSRect, atPlacement: NSPoint)](nsview/beginpage(in:atplacement:).md)
  Called at the beginning of each page, this method sets up the coordinate system so that a region inside the view’s bounds is translated to a specified location.
- [func dataWithEPS(inside: NSRect) -> Data](nsview/datawitheps(inside:).md)
  Returns EPS data that draws the region of the view within a specified rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](nsview/datawithpdf(inside:).md)
  Returns PDF data that draws the region of the view within a specified rectangle.
- [var printJobTitle: String](nsview/printjobtitle.md)
  The view’s print job title.
- [var pageHeader: NSAttributedString](nsview/pageheader.md)
  A default header string that includes the print job title and date.
- [var pageFooter: NSAttributedString](nsview/pagefooter.md)
  A default footer string that includes the current page number and page count.
- [func writeEPS(inside: NSRect, to: NSPasteboard)](nsview/writeeps(inside:to:).md)
  Writes EPS data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func writePDF(inside: NSRect, to: NSPasteboard)](nsview/writepdf(inside:to:).md)
  Writes PDF data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func drawSheetBorder(with: NSSize)](nsview/drawsheetborder(with:).md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each printed sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/drawpageborder(with:))*