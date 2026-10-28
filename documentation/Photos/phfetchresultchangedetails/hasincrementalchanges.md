# hasIncrementalChanges

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether changes to the fetch result can be described incrementally.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var hasIncrementalChanges: Bool { get }
```

```objc
@property (atomic, assign, readonly) BOOL hasIncrementalChanges;
```

## Discussion

If this value is `true`, use the [`insertedIndexes`](./insertedindexes.md), [`removedIndexes`](./removedindexes.md), and [`changedIndexes`](./changedindexes.md) properties (or the [`insertedObjects`](./insertedobjects.md), [`removedObjects`](./removedobjects.md), and [`changedObjects`](./changedobjects.md) properties) to find out which objects in the fetch result have been added, removed, or updated. You can also use the [`hasMoves`](./hasmoves.md) property and [`enumerateMoves(_:)`](./enumeratemoves%28_%29.md) method to find out which objects in the fetch result have been rearranged. These properties can be useful for updating a collection view or similar interface that displays the fetch result’s contents.

If this value is `false`, the fetch result is too different from its original state for incremental change information to be meaningful. Use the [`fetchResultAfterChanges`](./fetchresultafterchanges.md) property to get the fetch result’s current membership. (If displaying the fetch result’s contents, reload your user interface to match the new fetch result.)

## See Also

### Getting Change Information
- [var removedIndexes: IndexSet?](./removedindexes.md)
  The indexes from which objects have been removed from the fetch result.
- [var removedObjects: [ObjectType]](./removedobjects.md)
  The items that have been removed from the fetch result.
- [var insertedIndexes: IndexSet?](./insertedindexes.md)
  The indexes where new objects have been inserted in the fetch result.
- [var insertedObjects: [ObjectType]](./insertedobjects.md)
  The new items that have been inserted in the fetch result.
- [var changedIndexes: IndexSet?](./changedindexes.md)
  The indexes of objects in the fetch result whose content or metadata have been updated.
- [var changedObjects: [ObjectType]](./changedobjects.md)
  The objects in the fetch result whose content or metadata have been updated.
- [var hasMoves: Bool](./hasmoves.md)
  A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [func enumerateMoves((Int, Int) -> Void)](./enumeratemoves%28_%29.md)
  Runs the specified block for each case where an object has moved from one index to another in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/hasincrementalchanges)*