# allowsColumnSelection

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsColumnSelection: Bool { get set }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/swift/false), which prevents the user from selecting columns (if you create the table view in Interface Builder, the default value is [`true`](https://developer.apple.com/documentation/swift/true)). You can select columns programmatically regardless of this setting.

## See Also

- [var allowsColumnReordering: Bool](nstableview/allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](nstableview/allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](nstableview/allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowscolumnselection)*