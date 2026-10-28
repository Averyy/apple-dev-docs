# isButtonBordered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the combo box button displays a border.

**Availability**:
- macOS

## Declaration

```swift
var isButtonBordered: Bool { get set }
```

```objc
@property (getter=isButtonBordered) BOOL buttonBordered;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the button has a border; when it is [`false`](../../Swift/false.md), the button is borderless. For example, it is often useful when using a combo box in an [`NSTableView`](../nstableview.md) to display the button without a border.

## See Also

### Setting Display Attributes
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean value that indicates if the combo box displays a vertical scroller.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The spacing between cells in the combo box’s pop-up list.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the combo box’s pop-up list.
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/isbuttonbordered)*