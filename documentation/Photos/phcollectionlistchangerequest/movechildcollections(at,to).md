# moveChildCollections(at:to:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Moves the child collections at the specified indexes in the collection list to a new index.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func moveChildCollections(at indexes: IndexSet, to toIndex: Int)
```

```objc
- (void) moveChildCollectionsAtIndexes:(NSIndexSet *) indexes toIndex:(NSUInteger) toIndex;
```

## Discussion

When you call this method, Photos first removes the items in the `indexes` parameter from the collection, and then inserts them at the location specified by the `toIndex` parameter.

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [`init(for:childCollections:)`](./init%28for,childcollections%29.md) method before rearranging child collections.

## Parameters

- `indexes`: The indexes of the child collections to be moved in the collection list.
- `toIndex`: The index at which to place the moved child collections, relative to the collection list’s ordering after removing the items at `indexes`.

## See Also

### Managing Collections
- [func addChildCollections(any NSFastEnumeration)](./addchildcollections%28_%29.md)
  Adds the specified collections as children of the collection list.
- [func insertChildCollections(any NSFastEnumeration, at: IndexSet)](./insertchildcollections%28_,at%29.md)
  Inserts the specified collections into the collection list at the specified indexes.
- [func replaceChildCollections(at: IndexSet, withChildCollections: any NSFastEnumeration)](./replacechildcollections%28at,withchildcollections%29.md)
  Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [func removeChildCollections(any NSFastEnumeration)](./removechildcollections%28_%29.md)
  Removes the specified child collections from the collection list.
- [func removeChildCollections(at: IndexSet)](./removechildcollections%28at%29.md)
  Removes the child collections at the specified indexes from the collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/movechildcollections(at:to:))*