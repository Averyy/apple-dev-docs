# numberOfVisibleItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of visible items to display in the pop-up list at one time.

**Availability**:
- macOS

## Declaration

```swift
var numberOfVisibleItems: Int { get set }
```

```objc
@property NSInteger numberOfVisibleItems;
```

## Discussion

Use this property to configure how many items can be displayed at the same time. If the combo box has a scroller, the user can scroll to view additional items beyond the visible range.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.
### Setting Display Attributes
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean value indicating whether the combo box has a vertical scroller.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells in the pop-up list.
- [var isButtonBordered: Bool](./isbuttonbordered.md)
  A Boolean value indicating whether the combo box displays a border.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/numberofvisibleitems)*