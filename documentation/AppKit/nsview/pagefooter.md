# pageFooter

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A default footer string that includes the current page number and page count.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var pageFooter: NSAttributedString { get }
```

```objc
@property (copy, readonly) NSAttributedString * pageFooter;
```

#### Discussion

A printable view class can override this property to substitute its own content in place of the default value. You should not need to access the value of this property directly. The printing system accesses it once per page during printing.

Footers are generated only if the user defaults contain the key `NSPrintHeaderAndFooter` with the value [`true`](../../Swift/true.md).

## See Also

### Printing the View’s Content
- [func printView(Any?)](./printview%28_%29.md)
  This action method opens the Print panel, and if the user chooses an option other than canceling, prints the view and all its subviews to the device specified in the Print panel.
- [func beginPage(in: NSRect, atPlacement: NSPoint)](./beginpage%28in,atplacement%29.md)
  Called at the beginning of each page, this method sets up the coordinate system so that a region inside the view’s bounds is translated to a specified location.
- [func dataWithEPS(inside: NSRect) -> Data](./datawitheps%28inside%29.md)
  Returns EPS data that draws the region of the view within a specified rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](./datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the view within a specified rectangle.
- [var printJobTitle: String](./printjobtitle.md)
  The view’s print job title.
- [var pageHeader: NSAttributedString](./pageheader.md)
  A default header string that includes the print job title and date.
- [func writeEPS(inside: NSRect, to: NSPasteboard)](./writeeps%28inside,to%29.md)
  Writes EPS data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func writePDF(inside: NSRect, to: NSPasteboard)](./writepdf%28inside,to%29.md)
  Writes PDF data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func drawPageBorder(with: NSSize)](./drawpageborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each logical page.
- [func drawSheetBorder(with: NSSize)](./drawsheetborder%28with%29.md)
  Allows applications that use the AppKit pagination facility to draw additional marks on each printed sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/pagefooter)*