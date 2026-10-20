# isSelected(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether a specified index is currently selected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func isSelected(at index: Int) -> Bool
```

```objc
- (BOOL) isSelectedAtIndex:(NSInteger) index;
```

#### Return Value

A Boolean value indicating whether the specified index is currently selected.

#### Discussion

Use this method when you specify the [`NSToolbarItemGroup.SelectionMode.selectAny`](./selectionmode-swift.enum/selectany.md) selection mode for the grouped toolbar item to determine which subitems are currently selected.

## Parameters

- `index`: The index of the subitems in a grouped toolbar item.

## See Also

### Working with subitems
- [var subitems: [NSToolbarItem]](./subitems.md)
  The subitems of the grouped toolbar item.
- [var selectedIndex: Int](./selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func setSelected(Bool, at: Int)](./setselected%28_,at%29.md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/isselected(at:))*