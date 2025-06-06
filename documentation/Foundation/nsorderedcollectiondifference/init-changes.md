# init(changes:)

**Framework**: Foundation  
**Kind**: init

Creates an ordered collection difference using an array of ordered collection changes.

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
convenience init(changes: [NSOrderedCollectionChange])
```

## Parameters

- `changes`: An array of ordered collection changes.

## See Also

- [convenience init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?)](nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:).md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.
- [init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?, additionalChanges: [NSOrderedCollectionChange])](nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:).md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(changes:))*