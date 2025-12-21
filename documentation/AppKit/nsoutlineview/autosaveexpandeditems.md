# autosaveExpandedItems

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the expanded items are automatically saved across launches of the app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autosaveExpandedItems: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the outline view saves the state of its expanded items and restores that state the next time the user launches the app. (If the outline view’s [`autosaveName`](nstableview/autosavename-swift.property.md) property is `nil`, or if you have not implemented the [`outlineView(_:itemForPersistentObject:)`](nsoutlineviewdatasource/outlineview(_:itemforpersistentobject:).md) and [`outlineView(_:persistentObjectForItem:)`](nsoutlineviewdatasource/outlineview(_:persistentobjectforitem:).md) delegate methods, this setting is ignored and outline information is not saved.) The configuration data is saved separately for each user and for each app. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

You can have separate settings for the [`autosaveExpandedItems`](nsoutlineview/autosaveexpandeditems.md) and [`autosaveTableColumns`](nstableview/autosavetablecolumns.md) properties, so you could, for example, save expanded item information, but not table column positions.

## See Also

- [var autosaveTableColumns: Bool](nstableview/autosavetablecolumns.md)
  A Boolean value indicating whether the order and width of the table view’s columns are automatically saved.
- [var autosaveName: NSTableView.AutosaveName?](nstableview/autosavename-swift.property.md)
  The name under which table information is automatically saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/autosaveexpandeditems)*