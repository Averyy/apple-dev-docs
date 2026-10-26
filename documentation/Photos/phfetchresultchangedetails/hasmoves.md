# hasMoves

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether objects have been rearranged in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var hasMoves: Bool { get }
```

```objc
@property (atomic, assign, readonly) BOOL hasMoves;
```

#### Discussion

If this value is `true`, use the [`enumerateMoves(_:)`](./enumeratemoves%28_%29.md) method to find out which elements have been moved and what their new indexes are.

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
- [func enumerateMoves((Int, Int) -> Void)](./enumeratemoves%28_%29.md)
  Runs the specified block for each case where an object has moved from one index to another in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/hasmoves)*