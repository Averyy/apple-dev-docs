# knowsPageRange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the view handles page boundaries.

**Availability**:
- macOS

## Declaration

```swift
func knowsPageRange(_ range: NSRangePointer) -> Bool
```

```objc
- (BOOL) knowsPageRange:(NSRangePointer) range;
```

## Return Value

[`true`](../../Swift/true.md) if the view handles page boundaries; otherwise, [`false`](../../Swift/false.md).

## Discussion

Returns [`false`](../../Swift/false.md) if the view uses the default auto-pagination mechanism. The default implementation returns [`false`](../../Swift/false.md). Override this method if your class handles page boundaries.

## Parameters

- `range`: On return, holds the page range if [`true`](../../Swift/true.md) is returned directly. Page numbers are one-based—that is pages run from one to *N*.

## See Also

### Handling Pagination
- [var heightAdjustLimit: CGFloat](./heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [var widthAdjustLimit: CGFloat](./widthadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](./adjustpagewidthnew%28_,left,right,limit%29.md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](./adjustpageheightnew%28_,top,bottom,limit%29.md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func rectForPage(Int) -> NSRect](./rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](./locationofprintrect%28_%29.md)
  Invoked by [`printView(_:)`](./printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/knowspagerange(_:))*