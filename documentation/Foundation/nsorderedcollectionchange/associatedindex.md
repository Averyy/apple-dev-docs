# associatedIndex

**Framework**: Foundation  
**Kind**: property

When this property is set to a value other than [`NSNotFound`](nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var associatedIndex: Int { get }
```

#### Discussion

Pairs of changes with opposite types that refer to each other represent the index location of their counterpart with the [`associatedIndex`](nsorderedcollectionchange/associatedindex.md) property. The following example creates a diff where the object `@”Red”` moves from index `8` to index `3`:

```objc
NSOrderedCollectionDifference *diff = [[NSOrderedCollectionDifference alloc] initWithChanges:@[
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeRemove index:8 associatedIndex:3],
    [NSOrderedCollectionChange changeWithObject:@"Red" type:NSCollectionChangeInsert index:3 associatedIndex:8]
]];
```

A move pair can have a different `object` in its removal and insertion changes, which can imply that the change represents moving and changing or replacing an element. Diffs that [`controller(_:didChangeContentWith:)`](https://developer.apple.com/documentation/CoreData/NSFetchedResultsControllerDelegate/controller(_:didChangeContentWith:)-5ullb) passes to delegates of [`NSFetchedResultsController`](https://developer.apple.com/documentation/CoreData/NSFetchedResultsController) communicate that an object changed even when its position in the results is unaffected.

> **Note**:  Don’t ignore a move when the indexes of its changes are the same. The calculated difference from `@[@”A”, @”B”, @”C”]` to `@[@”C”, @”B”]` may legitimately produce a diff where the change removes the object at index 0 and the object at index 1 moves to index 1. Ignoring the move produces the incorrect result `@[@”B”, @”C”]`.

## See Also

- [var changeType: NSCollectionChangeType](nsorderedcollectionchange/changetype.md)
  The type of change.
- [var index: Int](nsorderedcollectionchange/index.md)
  The index location of the change.
- [var object: Any?](nsorderedcollectionchange/object.md)
  An object the change inserts or removes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/associatedindex)*