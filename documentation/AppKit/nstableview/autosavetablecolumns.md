# autosaveTableColumns

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the order and width of the table view’s columns are automatically saved.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autosaveTableColumns: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the table information is saved separately for each user and application under the name specified in the [`autosaveName`](nstableview/autosavename-swift.property.md) property. If you change the value of this property from [`false`](https://developer.apple.com/documentation/Swift/false) to [`true`](https://developer.apple.com/documentation/Swift/true), the table tries to read in any saved information and sets the order and width of this table view’s columns to match. If the [`autosaveName`](nstableview/autosavename-swift.property.md) property is `nil`, this setting is ignored and the table information is not read or saved.

When autosave is enabled, the table saves the table column width, the table column order, any applied sort descriptors, and the table column hidden state (in macOS 10.5 and later).

## See Also

- [var autosaveName: NSTableView.AutosaveName?](nstableview/autosavename-swift.property.md)
  The name under which table information is automatically saved.
- [NSTableView.AutosaveName](nstableview/autosavename-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/autosavetablecolumns)*