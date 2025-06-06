# moveItem(at:inParent:to:inParent:)

**Framework**: Appkit  
**Kind**: method

Moves an item at a given index in the given parent to a new index in a new parent.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func moveItem(at fromIndex: Int, inParent oldParent: Any?, to toIndex: Int, inParent newParent: Any?)
```

#### Discussion

This method parallels the [`moveRow(at:to:)`](nstableview/moverow(at:to:).md) method of [`NSTableView`](nstableview.md). The `newParent` can be the same as `oldParent` to reorder an item within the same parent.

> **Note**:  [`NSCell`](nscell.md)-based outline views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

You can call this method multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md)/[`endUpdates()`](nstableview/endupdates().md) block. Moving from an invalid index, or to an invalid index, throws an exception.

## Parameters

- `fromIndex`: Index of the item to be moved.
- `oldParent`: The parent of the item to be moved.
- `toIndex`: Index in the new parent to which the item is moved.
- `newParent`: The parent of the item after it is moved.

## See Also

- [func insertItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/insertitems(at:inparent:withanimation:).md)
  Inserts new items at the given indexes in the given parent with the specified optional animations.
- [func removeItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/removeitems(at:inparent:withanimation:).md)
  Removes items at the given indexes in the given parent with the specified optional animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/moveitem(at:inparent:to:inparent:))*