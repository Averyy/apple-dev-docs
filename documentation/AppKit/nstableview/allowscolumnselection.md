# allowsColumnSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.

**Availability**:
- macOS

## Declaration

```swift
var allowsColumnSelection: Bool { get set }
```

```objc
@property BOOL allowsColumnSelection;
```

#### Discussion

The default is [`false`](../../Swift/false.md), which prevents the user from selecting columns (if you create the table view in Interface Builder, the default value is [`true`](../../Swift/true.md)). You can select columns programmatically regardless of this setting.

## See Also

### Configuring Behavior
- [var allowsColumnReordering: Bool](./allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](./allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var usesAutomaticRowHeights: Bool](./usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowscolumnselection)*