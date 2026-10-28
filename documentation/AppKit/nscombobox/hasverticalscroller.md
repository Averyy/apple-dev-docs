# hasVerticalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the combo box has a vertical scroller.

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

When the value of this property is [`true`](../../Swift/true.md), the combo box displays a vertical scroller even when the pop-up list contains few enough items that a scroller is not needed. The default value of this property is [`true`](../../Swift/true.md).

If the value of this property is [`false`](../../Swift/false.md) and the combo box has more list items (either in its internal item list or from its data source) than are allowed by [`numberOfVisibleItems`](./numberofvisibleitems.md), only a subset of items are displayed. The `NSComboBox` class’ `scroll...` methods can be used to position this subset within the pop-up list.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.
### Setting Display Attributes
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells in the pop-up list.
- [var isButtonBordered: Bool](./isbuttonbordered.md)
  A Boolean value indicating whether the combo box displays a border.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the pop-up list.
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/hasverticalscroller)*