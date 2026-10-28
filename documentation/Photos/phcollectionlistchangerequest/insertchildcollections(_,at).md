# insertChildCollections(_:at:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Inserts the specified collections into the collection list at the specified indexes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func insertChildCollections(_ collections: any NSFastEnumeration, at indexes: IndexSet)
```

```objc
- (void) insertChildCollections:(id<NSFastEnumeration>) collections atIndexes:(NSIndexSet *) indexes;
```

## Discussion

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [`init(for:childCollections:)`](./init%28for,childcollections%29.md) method before inserting child collections.

For a detailed discussion of how the index set you specify maps to insertions in the collection list, see the similar [`NSMutableArray`](../../Foundation/nsmutablearray.md) method `insert`.

## Parameters

- `collections`: An array of [`PHCollection`](../phcollection.md) objects (asset collections or other collection lists) to be inserted into the collection list.
- `indexes`: The indexes at which the collections should be inserted. The count of locations in this index set must equal the count of collections.

## See Also

### Managing Collections
- [func addChildCollections(any NSFastEnumeration)](./addchildcollections%28_%29.md)
  Adds the specified collections as children of the collection list.
- [func moveChildCollections(at: IndexSet, to: Int)](./movechildcollections%28at,to%29.md)
  Moves the child collections at the specified indexes in the collection list to a new index.
- [func replaceChildCollections(at: IndexSet, withChildCollections: any NSFastEnumeration)](./replacechildcollections%28at,withchildcollections%29.md)
  Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [func removeChildCollections(any NSFastEnumeration)](./removechildcollections%28_%29.md)
  Removes the specified child collections from the collection list.
- [func removeChildCollections(at: IndexSet)](./removechildcollections%28at%29.md)
  Removes the child collections at the specified indexes from the collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/insertchildcollections(_:at:))*