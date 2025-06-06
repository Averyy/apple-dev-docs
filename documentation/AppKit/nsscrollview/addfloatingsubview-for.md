# addFloatingSubview(_:for:)

**Framework**: AppKit  
**Kind**: method

Adds a floating subview to the document view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func addFloatingSubview(_ view: NSView, for axis: NSEvent.GestureAxis)
```

#### Discussion

Floating subviews of the document view do not scroll like the rest of the document. Instead these views appear to float over the document. For example, see `NSTableView` floating group rows ([`floatsGroupRows`](nstableview/floatsgrouprows.md)).

`NSScrollView` ensures that any scrolling on the non-floating axis is performed visually synchronously with the document content.

> **Note**:  You are responsible for keeping track of the floating views and removing them via [`removeFromSuperview()`](nsview/removefromsuperview().md) when they should no longer float.

 You are responsible for keeping track of the floating views and removing them via [`removeFromSuperview()`](nsview/removefromsuperview().md) when they should no longer float.

## Parameters

- `view`: The view that can float.
- `axis`: The event gesture axis on which the view can float. A view can float on only one axis at a time.

## See Also

- [var contentView: NSClipView](nsscrollview/contentview.md)
  The scroll view’s content view, the view that clips the document view.
- [var documentView: NSView?](nsscrollview/documentview.md)
  The view the scroll view scrolls within its content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/addfloatingsubview(_:for:))*