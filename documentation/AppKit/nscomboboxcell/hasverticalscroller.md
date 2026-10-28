# hasVerticalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the combo box displays a vertical scroller.

**Availability**:
- macOS

## Declaration

```swift
var hasVerticalScroller: Bool { get set }
```

```objc
@property BOOL hasVerticalScroller;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the combo box displays a vertical scroller; when the value is [`false`](../../Swift/false.md), it does not. The default value of this property is [`true`](../../Swift/true.md). Note that the scroller is displayed even if the pop-up list contains fewer items than will fit in the area specified for display.

If you set this property to [`false`](../../Swift/false.md) and the combo box cell has more list items (either in its internal item list or from its data source) than are allowed by [`numberOfVisibleItems`](./numberofvisibleitems.md), only a subset are displayed. The [`NSComboBoxCell`](../nscomboboxcell.md) `scroll...` methods can be used to position this subset within the pop-up list.

## See Also

### Related Documentation
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.
### Setting Display Attributes
- [var isButtonBordered: Bool](./isbuttonbordered.md)
  A Boolean value that indicates whether the combo box button displays a border.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The spacing between cells in the combo box’s pop-up list.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the combo box’s pop-up list.
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/hasverticalscroller)*