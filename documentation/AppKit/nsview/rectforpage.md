# rectForPage(_:)

**Framework**: AppKit  
**Kind**: method

Implemented by subclasses to determine the portion of the view to be printed for the specified page number.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rectForPage(_ page: Int) -> NSRect
```

#### Return Value

A rectangle defining the region of the view to be printed for `pageNumber`. This method returns `NSZeroRect` if `pageNumber` is outside the view’s bounds.

#### Discussion

If the view responded [`true`](https://developer.apple.com/documentation/Swift/true) to an earlier [`knowsPageRange(_:)`](nsview/knowspagerange(_:).md) message, this method is invoked for each page it specified in the out parameters of that message. The view is later made to display this rectangle in order to generate the image for this page.

If an `NSView` object responds [`false`](https://developer.apple.com/documentation/Swift/false) to [`knowsPageRange(_:)`](nsview/knowspagerange(_:).md), this method isn’t invoked by the printing mechanism.

## Parameters

- `page`: An integer indicating a page number. Page numbers are one-based—that is pages run from one to  .

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
- [func locationOfPrintRect(NSRect) -> NSPoint](nsview/locationofprintrect(_:).md)
  Invoked by [`printView(_:)`](nsview/printview(_:).md) to determine the location of the region of the view being printed on the physical page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rectforpage(_:))*