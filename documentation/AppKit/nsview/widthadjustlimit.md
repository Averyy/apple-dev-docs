# widthAdjustLimit

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as small images or text columns from being divided across pages.

**Availability**:
- macOS

## Declaration

```swift
var widthAdjustLimit: CGFloat { get }
```

```objc
@property (readonly) CGFloat widthAdjustLimit;
```

#### Discussion

The value of this property is a floating point number in the range `0.0` to `1.0`. This fraction is used to calculate the right edge limit for a [`adjustPageWidthNew(_:left:right:limit:)`](./adjustpagewidthnew%28_,left,right,limit%29.md) message.

## See Also

### Handling Pagination
- [var heightAdjustLimit: CGFloat](./heightadjustlimit.md)
  The fraction of the page that can be pushed onto the next page during automatic pagination to prevent items such as lines of text from being divided across pages.
- [func adjustPageWidthNew(UnsafeMutablePointer<CGFloat>, left: CGFloat, right: CGFloat, limit: CGFloat)](./adjustpagewidthnew%28_,left,right,limit%29.md)
  Overridden by subclasses to adjust page width during automatic pagination.
- [func adjustPageHeightNew(UnsafeMutablePointer<CGFloat>, top: CGFloat, bottom: CGFloat, limit: CGFloat)](./adjustpageheightnew%28_,top,bottom,limit%29.md)
  Overridden by subclasses to adjust page height during automatic pagination.
- [func knowsPageRange(NSRangePointer) -> Bool](./knowspagerange%28_%29.md)
  Returns a Boolean value that indicates whether the view handles page boundaries.
- [func rectForPage(Int) -> NSRect](./rectforpage%28_%29.md)
  Implemented by subclasses to determine the portion of the view to be printed for the specified page number.
- [func locationOfPrintRect(NSRect) -> NSPoint](./locationofprintrect%28_%29.md)
  Invoked by [`printView(_:)`](./printview%28_%29.md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/widthadjustlimit)*