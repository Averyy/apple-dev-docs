# enumerateMoves(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Runs the specified block for each case where an object has moved from one index to another in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateMoves(_ handler: @escaping (Int, Int) -> Void)
```

```objc
- (void) enumerateMovesWithBlock:(void (^)(NSUInteger fromIndex, NSUInteger toIndex)) handler;
```

## Discussion

The `toIndex` parameter in the `handler` block is relative to the state of the fetch result after you’ve applied the changes described by the [`removedIndexes`](./removedindexes.md), [`insertedIndexes`](./insertedindexes.md) and [`changedIndexes`](./changedindexes.md) properties. Therefore, if you use this method to update a collection view or similar user interface displaying the contents of the fetch result, update your UI to reflect insertions, removals, and changes before you process moves.

## Parameters

- `handler`: A block that Photos calls to provide details about which objects in the fetch result have moved to which indexes.

  The block takes the following parameters:

  - **fromIndex**: The index of an object in the original fetch result.
  - **toIndex**: The index to which the object has moved in the new fetch result.

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
- [var changedIndexes: IndexSet?](./changedindexes.md)
  The indexes of objects in the fetch result whose content or metadata have been updated.
- [var changedObjects: [ObjectType]](./changedobjects.md)
  The objects in the fetch result whose content or metadata have been updated.
- [var hasMoves: Bool](./hasmoves.md)
  A Boolean value that indicates whether objects have been rearranged in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/enumeratemoves(_:))*