# init(insert:insertedObjects:remove:removedObjects:)

**Framework**: Foundation  
**Kind**: init

Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.

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
convenience init(insert inserts: IndexSet, insertedObjects: [Any]?, remove removes: IndexSet, removedObjects: [Any]?)
```

## Parameters

- `inserts`: An index set that represents the index values to associate with the objects in the provided array of inserted objects.
- `insertedObjects`: An array of objects the ordered collection difference will insert.
- `removes`: An index set that represents the index values to associate with the objects in the provided array of removed objects.
- `removedObjects`: An array of objects the ordered collection difference will remove.

## See Also

- [convenience init(changes: [NSOrderedCollectionChange])](nsorderedcollectiondifference/init(changes:).md)
  Creates an ordered collection difference using an array of ordered collection changes.
- [init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?, additionalChanges: [NSOrderedCollectionChange])](nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:).md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:))*