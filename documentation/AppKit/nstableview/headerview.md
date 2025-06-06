# headerView

**Framework**: AppKit  
**Kind**: property

The view object used to draw headers over columns.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var headerView: NSTableHeaderView? { get set }
```

#### Discussion

To configure a table without a header view or to remove the table view’s current header view, set the value of this property to `nil`. For more information about header views, see [`NSTableHeaderView`](nstableheaderview.md).

## See Also

- [var cornerView: NSView?](nstableview/cornerview.md)
  The view used to draw the area to the right of the column headers and above the vertical scroller of the enclosing scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/headerview)*