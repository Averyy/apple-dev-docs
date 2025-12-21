# isButtonBordered

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the combo box button displays a border.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isButtonBordered: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button has a border; when it is [`false`](https://developer.apple.com/documentation/Swift/false), the button is borderless. For example, it is often useful when using a combo box in an [`NSTableView`](nstableview.md) to display the button without a border.

## See Also

- [var hasVerticalScroller: Bool](nscomboboxcell/hasverticalscroller.md)
  A Boolean value that indicates if the combo box displays a vertical scroller.
- [var intercellSpacing: NSSize](nscomboboxcell/intercellspacing.md)
  The spacing between cells in the combo box’s pop-up list.
- [var itemHeight: CGFloat](nscomboboxcell/itemheight.md)
  The height of each item in the combo box’s pop-up list.
- [var numberOfVisibleItems: Int](nscomboboxcell/numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/isbuttonbordered)*