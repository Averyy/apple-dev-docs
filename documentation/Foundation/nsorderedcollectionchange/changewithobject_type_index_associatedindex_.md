# changeWithObject:type:index:associatedIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an change object that represents inserting or removing an object from an ordered collection at a specific index, matched with an associated location that infers a move within the collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (NSOrderedCollectionChange<id> *) changeWithObject:(ObjectType) anObject type:(NSCollectionChangeType) type index:(NSUInteger) index associatedIndex:(NSUInteger) associatedIndex;
```

## Return Value

An object that represents an indexed change to an ordered collection and references the object to be inserted or removed with an associated index that infers a move within the collection.

## Discussion

Pairs of changes with opposite types that refer to each other represent the index location of their counterpart with the [`associatedIndex`](./associatedindex.md) property. Initializing a [`NSOrderedCollectionDifference`](../nsorderedcollectiondifference.md) with broken associations (or associations that aren’t reflexive) will generate an exception. The following example creates a diff where the object `@”Red”` moves from index `8` to index `3`:

```objc
NSOrderedCollectionDifference *diff = [[NSOrderedCollectionDifference alloc] initWithChanges:@[
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeRemove index:8 associatedIndex:3],
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeInsert index:3 associatedIndex:8]
]];
```

A move pair can have a different `object` in its removal and insertion changes, which can imply that the change represents moving and changing or replacing an element. Diffs that [`controller(_:didChangeContentWith:)`](../../CoreData/nsfetchedresultscontrollerdelegate/controller%28_,didchangecontentwith%29-5ullb.md) passes to delegates of [`NSFetchedResultsController`](../../CoreData/nsfetchedresultscontroller.md) communicate that an object changed even when its position in the results is unaffected.

> **Note**:  Don’t ignore a move when the indexes of its changes are the same. The calculated difference from `@[@”A”, @”B”, @”C”]` to `@[@”C”, @”B”]` may legitimately produce a diff where the change removes the object at index 0 and the object at index 1 moves to index 1. Ignoring the move produces the incorrect result `@[@”B”, @”C”]`.

## Parameters

- `anObject`: An object to be removed or inserted by the change.
- `type`: The type of change
- `index`: The index location within an ordered collection where the change applies.
- `associatedIndex`: The index of the change’s counterpart of the opposite type in the diff.

## See Also

### Creating a Change
- [convenience init(object: Any?, type: NSCollectionChangeType, index: Int)](./init%28object,type,index%29.md)
  Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
- [init(object: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)](./init%28object,type,index,associatedindex%29.md)
  Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
- [+ changeWithObject:type:index:](./changewithobject_type_index_.md)
  Creates an change object that represents inserting or removing an object from an ordered collection at a specific index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/changewithobject:type:index:associatedindex:)*