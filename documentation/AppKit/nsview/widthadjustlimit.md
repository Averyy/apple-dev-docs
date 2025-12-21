# widthAdjustLimit

**Framework**: AppKit  
**Kind**: property

The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var widthAdjustLimit: CGFloat { get }
```

#### Discussion

The value of this property is a floating point number in the range `0.0` to `1.0`. This fraction is used to calculate the right edge limit for a [`adjustPageWidthNew(_:left:right:limit:)`](nsview/adjustpagewidthnew(_:left:right:limit:).md) message.

## See Also

- [var heightAdjustLimit: CGFloat](nsview/heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](nsview/adjustpagewidthnew(_:left:right:limit:).md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](nsview/adjustpageheightnew(_:top:bottom:limit:).md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](nsview/knowspagerange(_:).md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](nsview/rectforpage(_:).md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](nsview/locationofprintrect(_:).md)
  Invoked by [`printView(_:)`](nsview/printview(_:).md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/widthadjustlimit)*