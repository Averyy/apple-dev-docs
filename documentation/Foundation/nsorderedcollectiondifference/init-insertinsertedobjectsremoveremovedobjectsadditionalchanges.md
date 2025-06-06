# init(insert:insertedObjects:remove:removedObjects:additionalChanges:)

**Framework**: Foundation  
**Kind**: init

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

## Parameters

- `inserts`: An index set that represents the index values to associate with the objects in the provided array of inserted objects.
- `insertedObjects`: An array of objects the ordered collection difference will insert.
- `removes`: An index set that represents the index values to associate with the objects in the provided array of removed objects.
- `removedObjects`: An array of objects the ordered collection difference will remove.
- `changes`: An array of ordered collection changes.

## See Also

- [convenience init(changes: [NSOrderedCollectionChange])](nsorderedcollectiondifference/init(changes:).md)
  Creates an ordered collection difference using an array of ordered collection changes.
- [convenience init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?)](nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:).md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:))*