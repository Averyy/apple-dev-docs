# setSelected(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the selected state of a subitem in a grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func setSelected(_ selected: Bool, at index: Int)
```

```objc
- (void) setSelected:(BOOL) selected atIndex:(NSInteger) index;
```

## Parameters

- `selected`: If `true`, indicates whether to select a subitem, `false` otherwise.
- `index`: The index location of the subitem.

## See Also

### Working with subitems
- [var subitems: [NSToolbarItem]](./subitems.md)
  The subitems of the grouped toolbar item.
- [var selectedIndex: Int](./selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func isSelected(at: Int) -> Bool](./isselected%28at%29.md)
  Indicates whether a specified index is currently selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/setselected(_:at:))*