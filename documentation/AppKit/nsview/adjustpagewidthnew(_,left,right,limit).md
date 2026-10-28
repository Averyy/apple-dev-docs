# adjustPageWidthNew(_:left:right:limit:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to adjust page width during automatic pagination.

**Availability**:
- macOS

## Declaration

```swift
func adjustPageWidthNew(_ newRight: UnsafeMutablePointer<CGFloat>, left oldLeft: CGFloat, right oldRight: CGFloat, limit rightLimit: CGFloat)
```

```objc
- (void) adjustPageWidthNew:(CGFloat *) newRight left:(CGFloat) oldLeft right:(CGFloat) oldRight limit:(CGFloat) rightLimit;
```

## Discussion

This method is invoked by [`printView(_:)`](./printview%28_%29.md). The view can pull in the right edge and return the new value in `newRight`, allowing it to prevent items such as small images or text columns from being divided across pages. If `rightLimit` is exceeded, the pagination mechanism simply uses `rightLimit` for the right edge.

The default implementation of this method propagates the message to its subviews, allowing nested views to adjust page width for their drawing as well. An [`NSButton`](../nsbutton.md) object or other small view, for example, will nudge the right edge out if necessary to prevent itself from being cut in two (thereby pushing it onto an adjacent page). Subclasses should invoke `super`’s implementation, if desired, after first making their own adjustments.

## Parameters

- `newRight`: Returns by indirection a new [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value for the right edge of the pending page rectangle in the view’s coordinate system.
- `oldLeft`: A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value that sets the left edge of the pending page rectangle in the view’s coordinate system.
- `oldRight`: A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value that sets the right edge of the pending page rectangle in the view’s coordinate system.
- `rightLimit`: The leftmost [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value `newRight` can be set to, as calculated using the value of the [`widthAdjustLimit`](./widthadjustlimit.md) property.

## See Also

### Handling Pagination
- [var heightAdjustLimit: CGFloat](./heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](./widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](./adjustpageheightnew%28_,top,bottom,limit%29.md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](./knowspagerange%28_%29.md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](./rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](./locationofprintrect%28_%29.md)
  Invoked by [`printView(_:)`](./printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/adjustpagewidthnew(_:left:right:limit:))*