# hasVerticalScroller

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the combo box displays a vertical scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasVerticalScroller: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the combo box displays a vertical scroller; when the value is [`false`](https://developer.apple.com/documentation/Swift/false), it does not. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). Note that the scroller is displayed even if the pop-up list contains fewer items than will fit in the area specified for display.

If you set this property to [`false`](https://developer.apple.com/documentation/Swift/false) and the combo box cell has more list items (either in its internal item list or from its data source) than are allowed by [`numberOfVisibleItems`](nscomboboxcell/numberofvisibleitems.md), only a subset are displayed. The [`NSComboBoxCell`](nscomboboxcell.md) `scroll...` methods can be used to position this subset within the pop-up list.

## See Also

- [Combo Box Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i)
- [func scrollItemAtIndexToTop(Int)](nscomboboxcell/scrollitematindextotop(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.
- [func scrollItemAtIndexToVisible(Int)](nscomboboxcell/scrollitematindextovisible(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.
- [var isButtonBordered: Bool](nscomboboxcell/isbuttonbordered.md)
  A Boolean value that indicates whether the combo box button displays a border.
- [var intercellSpacing: NSSize](nscomboboxcell/intercellspacing.md)
  The spacing between cells in the combo box’s pop-up list.
- [var itemHeight: CGFloat](nscomboboxcell/itemheight.md)
  The height of each item in the combo box’s pop-up list.
- [var numberOfVisibleItems: Int](nscomboboxcell/numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/hasverticalscroller)*