# adjustPageHeightNew(_:top:bottom:limit:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to adjust page height during automatic pagination.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func adjustPageHeightNew(_ newBottom: UnsafeMutablePointer<CGFloat>, top oldTop: CGFloat, bottom oldBottom: CGFloat, limit bottomLimit: CGFloat)
```

#### Discussion

This method is invoked by [`printView(_:)`](nsview/printview(_:).md). The view can raise the bottom edge and return the new value in `newBottom`, allowing it to prevent items such as lines of text from being divided across pages. If `bottomLimit` is exceeded, the pagination mechanism simply uses `bottomLimit` for the bottom edge.

The default implementation of this method propagates the message to its subviews, allowing nested views to adjust page height for their drawing as well. An [`NSButton`](nsbutton.md) object or other small view, for example, will nudge the bottom edge up if necessary to prevent itself from being cut in two (thereby pushing it onto an adjacent page). Subclasses should invoke `super`’s implementation, if desired, after first making their own adjustments.

## Parameters

- `newBottom`: Returns by indirection a new   value for the bottom edge of the pending page rectangle in the view’s coordinate system.
- `oldTop`: A   value that sets the top edge of the pending page rectangle in the view’s coordinate system.
- `oldBottom`: A   value that sets the bottom edge of the pending page rectangle in the view’s coordinate system.
- `bottomLimit`: The topmost   value   can be set to, as calculated using the value of the   property.

## See Also

- [var heightAdjustLimit: CGFloat](nsview/heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](nsview/widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](nsview/adjustpagewidthnew(_:left:right:limit:).md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](nsview/knowspagerange(_:).md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](nsview/rectforpage(_:).md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](nsview/locationofprintrect(_:).md)
  Invoked by [`printView(_:)`](nsview/printview(_:).md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/adjustpageheightnew(_:top:bottom:limit:))*