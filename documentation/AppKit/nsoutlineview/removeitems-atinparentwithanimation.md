# removeItems(at:inParent:withAnimation:)

**Framework**: AppKit  
**Kind**: method

Removes items at the given indexes in the given parent with the specified optional animations.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func removeItems(at indexes: IndexSet, inParent parent: Any?, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

#### Discussion

This method parallels the [`removeRows(at:withAnimation:)`](nstableview/removerows(at:withanimation:).md) method of [`NSTableView`](nstableview.md) and is used in a way similar to the [`removeObjects(at:)`](https://developer.apple.com/documentation/Foundation/NSMutableArray/removeObjects(at:)) method of [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray). The method does nothing if `parent` is not expanded. If any of the child items is expanded, then all of its child rows are also be removed.

> **Note**:  [`NSCell`](nscell.md)-based outline views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

You can call this method multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md)/[`endUpdates()`](nstableview/endupdates().md) block; changes work just like modifying an array. Removing an item at an index beyond what is available throws an exception.

## Parameters

- `indexes`: Indexes of the items to be removed.
- `parent`: The parent of the items to be removed.
- `animationOptions`: Animated slide effects used when removing items.

## See Also

- [func insertItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/insertitems(at:inparent:withanimation:).md)
  Inserts new items at the given indexes in the given parent with the specified optional animations.
- [func moveItem(at: Int, inParent: Any?, to: Int, inParent: Any?)](nsoutlineview/moveitem(at:inparent:to:inparent:).md)
  Moves an item at a given index in the given parent to a new index in a new parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/removeitems(at:inparent:withanimation:))*