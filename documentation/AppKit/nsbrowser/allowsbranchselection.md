# allowsBranchSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can select branch items.

**Availability**:
- macOS

## Declaration

```swift
var allowsBranchSelection: Bool { get set }
```

```objc
@property BOOL allowsBranchSelection;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user can select branch items when multiple selection is enabled.

## See Also

### Managing Selection Behavior
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](./selectedrowindexes%28incolumn%29.md)
  Provides the indexes of the selected rows in a given column of the browser.
- [func selectRowIndexes(IndexSet, inColumn: Int)](./selectrowindexes%28_,incolumn%29.md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](./allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/allowsbranchselection)*