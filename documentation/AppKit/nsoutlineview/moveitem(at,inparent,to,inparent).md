# moveItem(at:inParent:to:inParent:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves an item at a given index in the given parent to a new index in a new parent.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func moveItem(at fromIndex: Int, inParent oldParent: Any?, to toIndex: Int, inParent newParent: Any?)
```

```objc
- (void) moveItemAtIndex:(NSInteger) fromIndex inParent:(id) oldParent toIndex:(NSInteger) toIndex inParent:(id) newParent;
```

## Discussion

This method parallels the [`moveRow(at:to:)`](../nstableview/moverow%28at,to%29.md) method of [`NSTableView`](../nstableview.md). The `newParent` can be the same as `oldParent` to reorder an item within the same parent.

> **Note**:  [`NSCell`](../nscell.md)-based outline views must first call [`beginUpdates()`](../nstableview/beginupdates%28%29.md) before calling this method.

You can call this method multiple times within the same [`beginUpdates()`](../nstableview/beginupdates%28%29.md)/[`endUpdates()`](../nstableview/endupdates%28%29.md) block. Moving from an invalid index, or to an invalid index, throws an exception.

## Parameters

- `fromIndex`: Index of the item to be moved.
- `oldParent`: The parent of the item to be moved.
- `toIndex`: Index in the new parent to which the item is moved.
- `newParent`: The parent of the item after it is moved.

## See Also

### Manipulating Items
- [func insertItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](./insertitems%28at,inparent,withanimation%29.md)
  Inserts new items at the given indexes in the given parent with the specified optional animations.
- [func removeItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](./removeitems%28at,inparent,withanimation%29.md)
  Removes items at the given indexes in the given parent with the specified optional animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/moveitem(at:inparent:to:inparent:))*