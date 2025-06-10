# insertItems(at:inParent:withAnimation:)

**Framework**: AppKit  
**Kind**: method

Inserts new items at the given indexes in the given parent with the specified optional animations.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func insertItems(at indexes: IndexSet, inParent parent: Any?, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

#### Discussion

This method parallels the [`insertRows(at:withAnimation:)`](nstableview/insertrows(at:withanimation:).md) method of [`NSTableView`](nstableview.md) and is used in a way similar to the [`insert(_:at:)`](https://developer.apple.com/documentation/Foundation/NSMutableArray/insert(_:at:)-73pln) method of [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray). The method does nothing if `parent` is not expanded. The actual item values are determined by the data source’s [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md) method (which is called only after [`endUpdates()`](nstableview/endupdates().md) to ensure data source integrity).

> **Note**:  [`NSCell`](nscell.md)-based outline views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

You can call this method multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md)/[`endUpdates()`](nstableview/endupdates().md) block; new insertions move previously inserted new items, just like modifying an array. Inserting an index beyond what is available throws an exception.

## Parameters

- `indexes`: Indexes at which to insert items.
- `parent`: The parent for the items, or   if the parent is the root.
- `animationOptions`: Animated slide effects used when inserting items.

## See Also

- [func moveItem(at: Int, inParent: Any?, to: Int, inParent: Any?)](nsoutlineview/moveitem(at:inparent:to:inparent:).md)
  Moves an item at a given index in the given parent to a new index in a new parent.
- [func removeItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/removeitems(at:inparent:withanimation:).md)
  Removes items at the given indexes in the given parent with the specified optional animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/insertitems(at:inparent:withanimation:))*