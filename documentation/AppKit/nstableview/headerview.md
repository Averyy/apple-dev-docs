# headerView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view object used to draw headers over columns.

**Availability**:
- macOS

## Declaration

```swift
var headerView: NSTableHeaderView? { get set }
```

```objc
@property (strong, nullable) NSTableHeaderView * headerView;
```

#### Discussion

To configure a table without a header view or to remove the table view’s current header view, set the value of this property to `nil`. For more information about header views, see [`NSTableHeaderView`](../nstableheaderview.md).

## See Also

### Setting Auxiliary Views
- [var cornerView: NSView?](./cornerview.md)
  The view used to draw the area to the right of the column headers and above the vertical scroller of the enclosing scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/headerview)*