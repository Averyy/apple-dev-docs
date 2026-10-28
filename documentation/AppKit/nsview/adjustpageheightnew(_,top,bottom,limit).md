# adjustPageHeightNew(_:top:bottom:limit:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to adjust page height during automatic pagination.

**Availability**:
- macOS

## Declaration

```swift
func adjustPageHeightNew(_ newBottom: UnsafeMutablePointer<CGFloat>, top oldTop: CGFloat, bottom oldBottom: CGFloat, limit bottomLimit: CGFloat)
```

```objc
- (void) adjustPageHeightNew:(CGFloat *) newBottom top:(CGFloat) oldTop bottom:(CGFloat) oldBottom limit:(CGFloat) bottomLimit;
```

## Discussion

This method is invoked by [`printView(_:)`](./printview%28_%29.md). The view can raise the bottom edge and return the new value in `newBottom`, allowing it to prevent items such as lines of text from being divided across pages. If `bottomLimit` is exceeded, the pagination mechanism simply uses `bottomLimit` for the bottom edge.

The default implementation of this method propagates the message to its subviews, allowing nested views to adjust page height for their drawing as well. An [`NSButton`](../nsbutton.md) object or other small view, for example, will nudge the bottom edge up if necessary to prevent itself from being cut in two (thereby pushing it onto an adjacent page). Subclasses should invoke `super`’s implementation, if desired, after first making their own adjustments.

## Parameters

- `newBottom`: Returns by indirection a new [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value for the bottom edge of the pending page rectangle in the view’s coordinate system.
- `oldTop`: A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value that sets the top edge of the pending page rectangle in the view’s coordinate system.
- `oldBottom`: A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value that sets the bottom edge of the pending page rectangle in the view’s coordinate system.
- `bottomLimit`: The topmost [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value `newBottom` can be set to, as calculated using the value of the [`heightAdjustLimit`](./heightadjustlimit.md) property.

## See Also

### Handling Pagination
- [var heightAdjustLimit: CGFloat](./heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](./widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](./adjustpagewidthnew%28_,left,right,limit%29.md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](./knowspagerange%28_%29.md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](./rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](./locationofprintrect%28_%29.md)
  Invoked by [`printView(_:)`](./printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/adjustpageheightnew(_:top:bottom:limit:))*