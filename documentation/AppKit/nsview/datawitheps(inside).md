# dataWithEPS(inside:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns EPS data that draws the region of the view within a specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func dataWithEPS(inside rect: NSRect) -> Data
```

```objc
- (NSData *) dataWithEPSInsideRect:(NSRect) rect;
```

## Discussion

This data can be placed on an [`NSPasteboard`](../nspasteboard.md) object, written to a file, or used to create an [`NSImage`](../nsimage.md) object.

## Parameters

- `rect`: A rectangle defining the region.

## See Also

### Printing the View’s Content
- [func printView(Any?)](./printview%28_%29.md)
  This action method opens the Print panel, and if the user chooses an option other than canceling, prints the view and all its subviews to the device specified in the Print panel.
- [func beginPage(in: NSRect, atPlacement: NSPoint)](./beginpage%28in,atplacement%29.md)
  Called at the beginning of each page, this method sets up the coordinate system so that a region inside the view’s bounds is translated to a specified location.
- [func dataWithPDF(inside: NSRect) -> Data](./datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the view within a specified rectangle.
- [var printJobTitle: String](./printjobtitle.md)
  The view’s print job title.
- [var pageHeader: NSAttributedString](./pageheader.md)
  A default header string that includes the print job title and date.
- [var pageFooter: NSAttributedString](./pagefooter.md)
  A default footer string that includes the current page number and page count.
- [func writeEPS(inside: NSRect, to: NSPasteboard)](./writeeps%28inside,to%29.md)
  Writes EPS data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func writePDF(inside: NSRect, to: NSPasteboard)](./writepdf%28inside,to%29.md)
  Writes PDF data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func drawPageBorder(with: NSSize)](./drawpageborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each logical page.
- [func drawSheetBorder(with: NSSize)](./drawsheetborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each printed sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/datawitheps(inside:))*