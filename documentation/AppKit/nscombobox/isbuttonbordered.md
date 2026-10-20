# isButtonBordered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the combo box displays a border.

**Availability**:
- macOS

## Declaration

```swift
var isButtonBordered: Bool { get set }
```

```objc
@property (getter=isButtonBordered) BOOL buttonBordered;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the combo box displays a border. For example, when displaying a combo box in a table, it is often useful to display the combo box without a border. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Setting Display Attributes
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean value indicating whether the combo box has a vertical scroller.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells in the pop-up list.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the pop-up list.
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/isbuttonbordered)*