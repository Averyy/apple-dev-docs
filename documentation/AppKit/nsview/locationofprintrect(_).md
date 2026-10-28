# locationOfPrintRect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked by [`printView(_:)`](./printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.

**Availability**:
- macOS

## Declaration

```swift
func locationOfPrintRect(_ rect: NSRect) -> NSPoint
```

```objc
- (NSPoint) locationOfPrintRect:(NSRect) rect;
```

## Return Value

A point to be used for setting the origin for `aRect`, whose size the view can examine in order to properly place it. It is expressed in the default coordinate system of the page.

## Discussion

The default implementation places `aRect` according to the status of the [`NSPrintInfo`](../nsprintinfo.md) object for the print job. By default it places the image in the upper-left corner of the page, but if the `NSPrintInfo` methods [`isHorizontallyCentered`](../nsprintinfo/ishorizontallycentered.md) or [`isVerticallyCentered`](../nsprintinfo/isverticallycentered.md) return [`true`](../../Swift/true.md), it centers a single-page image along the appropriate axis. A multiple-page document, however, is always placed so the divided pieces can be assembled at their edges.

## Parameters

- `rect`: A rectangle defining a region of the view; it is expressed in the default coordinate system of the page.

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
- [func knowsPageRange(NSRangePointer) -> Bool](./knowspagerange%28_%29.md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](./rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/locationofprintrect(_:))*