# knowsPageRange(_:)

**Framework**: AppKit  
**Kind**: method

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the view handles page boundaries, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func knowsPageRange(_ range: NSRangePointer) -> Bool
```

#### Discussion

Returns [`false`](https://developer.apple.com/documentation/swift/false) if the view uses the default auto-pagination mechanism. The default implementation returns [`false`](https://developer.apple.com/documentation/swift/false). Override this method if your class handles page boundaries.

## Parameters

- `range`: On return, holds the page range if   is returned directly. Page numbers are one-based—that is pages run from one to  .

## See Also

- [var heightAdjustLimit: CGFloat](nsview/heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](nsview/widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](nsview/adjustpagewidthnew(_:left:right:limit:).md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](nsview/adjustpageheightnew(_:top:bottom:limit:).md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func rectForPage(Int) -> NSRect](nsview/rectforpage(_:).md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](nsview/locationofprintrect(_:).md)
  Invoked by [`printView(_:)`](nsview/printview(_:).md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/knowspagerange(_:))*