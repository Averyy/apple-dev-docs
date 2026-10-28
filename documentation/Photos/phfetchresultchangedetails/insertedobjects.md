# insertedObjects

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The new items that have been inserted in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var insertedObjects: [ObjectType] { get }
```

```objc
@property (atomic, strong, readonly) NSArray<PHObject *> * insertedObjects;
```

## Discussion

This array can contain [`PHAsset`](../phasset.md), [`PHAssetCollection`](../phassetcollection.md), or [`PHCollectionList`](../phcollectionlist.md) objects, or some combination thereof.

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
- [var changedIndexes: IndexSet?](./changedindexes.md)
  The indexes of objects in the fetch result whose content or metadata have been updated.
- [var changedObjects: [ObjectType]](./changedobjects.md)
  The objects in the fetch result whose content or metadata have been updated.
- [var hasMoves: Bool](./hasmoves.md)
  A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [func enumerateMoves((Int, Int) -> Void)](./enumeratemoves%28_%29.md)
  Runs the specified block for each case where an object has moved from one index to another in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/insertedobjects)*