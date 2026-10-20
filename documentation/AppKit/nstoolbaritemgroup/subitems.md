# subitems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The subitems of the grouped toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var subitems: [NSToolbarItem] { get set }
```

```objc
@property (copy) NSArray<__kindof NSToolbarItem *> * subitems;
```

#### Discussion

By default, an [`NSToolbarItemGroup`](../nstoolbaritemgroup.md) instance has an empty array of subitems.

## See Also

### Related Documentation
- [class NSToolbarItemGroup](../nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
### Working with subitems
- [var selectedIndex: Int](./selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func isSelected(at: Int) -> Bool](./isselected%28at%29.md)
  Indicates whether a specified index is currently selected.
- [func setSelected(Bool, at: Int)](./setselected%28_,at%29.md)
  Sets the selected state of a subitem in a grouped toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/subitems)*