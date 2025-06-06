# cornerView

**Framework**: AppKit  
**Kind**: property

The view used to draw the area to the right of the column headers and above the vertical scroller of the enclosing scroll view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var cornerView: NSView? { get set }
```

#### Return Value

The view used to draw the area to the right of the column headers and above the vertical scroller of the enclosing `NSScrollView` object.

#### Discussion

The default corner view draws a bezeled rectangle using a blank [`NSTableHeaderCell`](nstableheadercell.md) object, but you can replace it with a custom view that displays an image, or with a control that can handle mouse events, such as a Select All button. Your custom corner view should be as wide as a vertical [`NSScroller`](nsscroller.md) object and as tall as the header view of the table view.

## See Also

- [var headerView: NSTableHeaderView?](nstableview/headerview.md)
  The view object used to draw headers over columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/cornerview)*