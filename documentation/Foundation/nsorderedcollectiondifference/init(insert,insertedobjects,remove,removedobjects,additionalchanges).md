# init(insert:insertedObjects:remove:removedObjects:additionalChanges:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.

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
init(insert inserts: IndexSet, insertedObjects: [Any]?, remove removes: IndexSet, removedObjects: [Any]?, additionalChanges changes: [NSOrderedCollectionChange])
```

```objc
- (instancetype) initWithInsertIndexes:(NSIndexSet *) inserts insertedObjects:(NSArray<id> *) insertedObjects removeIndexes:(NSIndexSet *) removes removedObjects:(NSArray<id> *) removedObjects additionalChanges:(NSArray<NSOrderedCollectionChange<id> *> *) changes;
```

## Parameters

- `inserts`: An index set that represents the index values to associate with the objects in the provided array of inserted objects.
- `insertedObjects`: An array of objects the ordered collection difference will insert.
- `removes`: An index set that represents the index values to associate with the objects in the provided array of removed objects.
- `removedObjects`: An array of objects the ordered collection difference will remove.
- `changes`: An array of ordered collection changes.

## See Also

### Creating a Collection Difference Object
- [convenience init(changes: [NSOrderedCollectionChange])](./init%28changes%29.md)
  Creates an ordered collection difference using an array of ordered collection changes.
- [convenience init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?)](./init%28insert,insertedobjects,remove,removedobjects%29.md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:))*