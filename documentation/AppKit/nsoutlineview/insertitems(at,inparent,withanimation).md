# insertItems(at:inParent:withAnimation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts new items at the given indexes in the given parent with the specified optional animations.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func insertItems(at indexes: IndexSet, inParent parent: Any?, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

```objc
- (void) insertItemsAtIndexes:(NSIndexSet *) indexes inParent:(id) parent withAnimation:(NSTableViewAnimationOptions) animationOptions;
```

#### Discussion

This method parallels the [`insertRows(at:withAnimation:)`](../nstableview/insertrows%28at,withanimation%29.md) method of [`NSTableView`](../nstableview.md) and is used in a way similar to the [`insert(_:at:)`](../../Foundation/nsmutablearray/insert%28_,at%29-73pln.md) method of [`NSMutableArray`](../../Foundation/nsmutablearray.md). The method does nothing if `parent` is not expanded. The actual item values are determined by the data source’s [`outlineView(_:child:ofItem:)`](../nsoutlineviewdatasource/outlineview%28_,child,ofitem%29.md) method (which is called only after [`endUpdates()`](../nstableview/endupdates%28%29.md) to ensure data source integrity).

> **Note**:  [`NSCell`](../nscell.md)-based outline views must first call [`beginUpdates()`](../nstableview/beginupdates%28%29.md) before calling this method.

You can call this method multiple times within the same [`beginUpdates()`](../nstableview/beginupdates%28%29.md)/[`endUpdates()`](../nstableview/endupdates%28%29.md) block; new insertions move previously inserted new items, just like modifying an array. Inserting an index beyond what is available throws an exception.

## Parameters

- `indexes`: Indexes at which to insert items.
- `parent`: The parent for the items, or `nil` if the parent is the root.
- `animationOptions`: Animated slide effects used when inserting items.

## See Also

### Manipulating Items
- [func moveItem(at: Int, inParent: Any?, to: Int, inParent: Any?)](./moveitem%28at,inparent,to,inparent%29.md)
  Moves an item at a given index in the given parent to a new index in a new parent.
- [func removeItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](./removeitems%28at,inparent,withanimation%29.md)
  Removes items at the given indexes in the given parent with the specified optional animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/insertitems(at:inparent:withanimation:))*