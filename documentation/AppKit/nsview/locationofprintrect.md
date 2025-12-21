# locationOfPrintRect(_:)

**Framework**: AppKit  
**Kind**: method

Invoked by [`printView(_:)`](nsview/printview(_:).md) to determine the location of the region of the view being printed on the physical page.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func locationOfPrintRect(_ rect: NSRect) -> NSPoint
```

#### Return Value

A point to be used for setting the origin for `aRect`, whose size the view can examine in order to properly place it. It is expressed in the default coordinate system of the page.

#### Discussion

The default implementation places `aRect` according to the status of the [`NSPrintInfo`](nsprintinfo.md) object for the print job. By default it places the image in the upper-left corner of the page, but if the `NSPrintInfo` methods [`isHorizontallyCentered`](nsprintinfo/ishorizontallycentered.md) or [`isVerticallyCentered`](nsprintinfo/isverticallycentered.md) return [`true`](https://developer.apple.com/documentation/Swift/true), it centers a single-page image along the appropriate axis. A multiple-page document, however, is always placed so the divided pieces can be assembled at their edges.

## Parameters

- `rect`: A rectangle defining a region of the view; it is expressed in the default coordinate system of the page.

## See Also

- [var heightAdjustLimit: CGFloat](nsview/heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](nsview/widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](nsview/adjustpagewidthnew(_:left:right:limit:).md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](nsview/adjustpageheightnew(_:top:bottom:limit:).md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](nsview/knowspagerange(_:).md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](nsview/rectforpage(_:).md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/locationofprintrect(_:))*