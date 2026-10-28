# selectedIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index value for the most recently selected subitem of a grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var selectedIndex: Int { get set }
```

```objc
@property NSInteger selectedIndex;
```

## Discussion

When using the [`NSToolbarItemGroup.SelectionMode.selectAny`](./selectionmode-swift.enum/selectany.md) or [`NSToolbarItemGroup.SelectionMode.momentary`](./selectionmode-swift.enum/momentary.md) selection mode, don’t assume that this value represents the selected subitem. This method returns the index of the most recently selected subitem.

To determine if a specific subitem of a grouped toolbar item is selected, use the [`isSelected(at:)`](./isselected%28at%29.md) method.

## See Also

### Working with subitems
- [var subitems: [NSToolbarItem]](./subitems.md)
  The subitems of the grouped toolbar item.
- [func isSelected(at: Int) -> Bool](./isselected%28at%29.md)
  Indicates whether a specified index is currently selected.
- [func setSelected(Bool, at: Int)](./setselected%28_,at%29.md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/selectedindex)*