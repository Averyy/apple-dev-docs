# allowsTypeSelect

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the browser allows keystroke-based selection (type select).

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var allowsTypeSelect: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the browser allows keystroke-based selection. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsBranchSelection: Bool](nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](nsbrowser/allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](nsbrowser/selectedrowindexes(incolumn:).md)
  Provides the indexes of the selected rows in a given column of the browser.
- [func selectRowIndexes(IndexSet, inColumn: Int)](nsbrowser/selectrowindexes(_:incolumn:).md)
  Specifies the selected rows in a given column of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/allowstypeselect)*