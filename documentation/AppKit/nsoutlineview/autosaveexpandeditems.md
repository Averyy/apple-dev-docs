# autosaveExpandedItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the expanded items are automatically saved across launches of the app.

**Availability**:
- macOS

## Declaration

```swift
var autosaveExpandedItems: Bool { get set }
```

```objc
@property BOOL autosaveExpandedItems;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the outline view saves the state of its expanded items and restores that state the next time the user launches the app. (If the outline view’s [`autosaveName`](../nstableview/autosavename-swift.property.md) property is `nil`, or if you have not implemented the [`outlineView(_:itemForPersistentObject:)`](../nsoutlineviewdatasource/outlineview%28_,itemforpersistentobject%29.md) and [`outlineView(_:persistentObjectForItem:)`](../nsoutlineviewdatasource/outlineview%28_,persistentobjectforitem%29.md) delegate methods, this setting is ignored and outline information is not saved.) The configuration data is saved separately for each user and for each app. The default value of this property is [`false`](../../Swift/false.md).

You can have separate settings for the [`autosaveExpandedItems`](./autosaveexpandeditems.md) and [`autosaveTableColumns`](../nstableview/autosavetablecolumns.md) properties, so you could, for example, save expanded item information, but not table column positions.

## See Also

### Related Documentation
- [var autosaveTableColumns: Bool](../nstableview/autosavetablecolumns.md)
  A Boolean value indicating whether the order and width of the table view’s columns are automatically saved.
- [var autosaveName: NSTableView.AutosaveName?](../nstableview/autosavename-swift.property.md)
  The name under which table information is automatically saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/autosaveexpandeditems)*