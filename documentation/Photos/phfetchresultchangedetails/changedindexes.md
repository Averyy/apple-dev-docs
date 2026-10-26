# changedIndexes

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The indexes of objects in the fetch result whose content or metadata have been updated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var changedIndexes: IndexSet? { get }
```

```objc
@property (atomic, strong, readonly, nullable) NSIndexSet * changedIndexes;
```

#### Discussion

Use this index set to update elements in a collection view or similar user interface that displays the contents of the fetch result. These indexes are relative to the original fetch result (the [`fetchResultBeforeChanges`](./fetchresultbeforechanges.md) property) after you’ve applied the changes described by the [`removedIndexes`](./removedindexes.md) and [`insertedIndexes`](./insertedindexes.md) properties; when updating your app’s interface, apply changes after removals and insertions and before moves.

> ⚠️ **Warning**:  Don’t map `changedIndexes` directly to [`UICollectionView`](../../UIKit/uicollectionview.md) item indices in batch updates. Use these indices to reconfigure the corresponding cells after [`performBatchUpdates(_:completion:)`](../../UIKit/uicollectionview/performbatchupdates%28_,completion%29.md). [`UICollectionView`](../../UIKit/uicollectionview.md) and [`UITableView`](../../UIKit/uitableview.md) expect the `changedIndexes` to be in the *before* state, while PhotoKit provides them in the *after* state, resulting in a crash if your app performs insertions and deletions at the same time as the changes.

If the [`hasIncrementalChanges`](./hasincrementalchanges.md) property’s value is `false`, this property’s value is `nil`.

## See Also

### Getting Change Information
- [var hasIncrementalChanges: Bool](./hasincrementalchanges.md)
  A Boolean value that indicates whether changes to the fetch result can be described incrementally.
- [var removedIndexes: IndexSet?](./removedindexes.md)
  The indexes from which objects have been removed from the fetch result.
- [var removedObjects: [ObjectType]](./removedobjects.md)
  The items that have been removed from the fetch result.
- [var insertedIndexes: IndexSet?](./insertedindexes.md)
  The indexes where new objects have been inserted in the fetch result.
- [var insertedObjects: [ObjectType]](./insertedobjects.md)
  The new items that have been inserted in the fetch result.
- [var changedObjects: [ObjectType]](./changedobjects.md)
  The objects in the fetch result whose content or metadata have been updated.
- [var hasMoves: Bool](./hasmoves.md)
  A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [func enumerateMoves((Int, Int) -> Void)](./enumeratemoves%28_%29.md)
  Runs the specified block for each case where an object has moved from one index to another in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/changedindexes)*