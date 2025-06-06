# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the user can select multiple items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the browser allows the user to select multiple items at once.

## See Also

- [var allowsBranchSelection: Bool](nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](nsbrowser/selectedrowindexes(incolumn:).md)
  Provides the indexes of the selected rows in a given column of the browser.
- [func selectRowIndexes(IndexSet, inColumn: Int)](nsbrowser/selectrowindexes(_:incolumn:).md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/allowsmultipleselection)*