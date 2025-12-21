# hasVerticalScroller

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the combo box has a vertical scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasVerticalScroller: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the combo box displays a vertical scroller even when the pop-up list contains few enough items that a scroller is not needed. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) and the combo box has more list items (either in its internal item list or from its data source) than are allowed by [`numberOfVisibleItems`](nscombobox/numberofvisibleitems.md), only a subset of items are displayed. The `NSComboBox` class’ `scroll...` methods can be used to position this subset within the pop-up list.

## See Also

- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.
- [func scrollItemAtIndexToTop(Int)](nscombobox/scrollitematindextotop(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [Combo Box Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i)
- [func scrollItemAtIndexToVisible(Int)](nscombobox/scrollitematindextovisible(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.
- [var intercellSpacing: NSSize](nscombobox/intercellspacing.md)
  The horizontal and vertical spacing between cells in the pop-up list.
- [var isButtonBordered: Bool](nscombobox/isbuttonbordered.md)
  A Boolean value indicating whether the combo box displays a border.
- [var itemHeight: CGFloat](nscombobox/itemheight.md)
  The height of each item in the pop-up list.
- [var numberOfVisibleItems: Int](nscombobox/numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/hasverticalscroller)*