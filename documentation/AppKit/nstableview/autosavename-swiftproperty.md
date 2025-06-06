# autosaveName

**Framework**: AppKit  
**Kind**: property

The name under which table information is automatically saved.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autosaveName: NSTableView.AutosaveName? { get set }
```

#### Discussion

The table information is saved separately in user defaults for each user and for each application that user uses. If no name has been set, the value of this property is `nil`. Even when a table view has an autosave name, it only saves the table information when the [`autosaveTableColumns`](nstableview/autosavetablecolumns.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

If you change the value of this property to a new name, the table reads in any saved information and sets the order and width of this table view’s columns to match. Setting the name to `nil` removes any previously stored state from the user defaults.

## See Also

- [var autosaveTableColumns: Bool](nstableview/autosavetablecolumns.md)
  A Boolean value indicating whether the order and width of the table view’s columns are automatically saved.
- [NSTableView.AutosaveName](nstableview/autosavename-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/autosavename-swift.property)*