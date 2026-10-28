# intercellSpacing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The horizontal and vertical spacing between cells in the pop-up list.

**Availability**:
- macOS

## Declaration

```swift
var intercellSpacing: NSSize { get set }
```

```objc
@property NSSize intercellSpacing;
```

## Discussion

Spacing values are measured in points. The default spacing is (`3.0`, `2.0`).

## See Also

### Setting Display Attributes
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean value indicating whether the combo box has a vertical scroller.
- [var isButtonBordered: Bool](./isbuttonbordered.md)
  A Boolean value indicating whether the combo box displays a border.
- [var itemHeight: CGFloat](./itemheight.md)
  The height of each item in the pop-up list.
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/intercellspacing)*