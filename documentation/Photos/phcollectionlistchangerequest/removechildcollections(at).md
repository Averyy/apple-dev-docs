# removeChildCollections(at:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Removes the child collections at the specified indexes from the collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func removeChildCollections(at indexes: IndexSet)
```

```objc
- (void) removeChildCollectionsAtIndexes:(NSIndexSet *) indexes;
```

## Discussion

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [`init(for:childCollections:)`](./init%28for,childcollections%29.md) method before removing child collections. To remove objects based on their identities (without regard to their indexes in the collection), use the [`removeChildCollections(_:)`](./removechildcollections%28_%29.md) method.

## Parameters

- `indexes`: The indexes of the child collections to be removed from the collection list.

## See Also

### Managing Collections
- [func addChildCollections(any NSFastEnumeration)](./addchildcollections%28_%29.md)
  Adds the specified collections as children of the collection list.
- [func insertChildCollections(any NSFastEnumeration, at: IndexSet)](./insertchildcollections%28_,at%29.md)
  Inserts the specified collections into the collection list at the specified indexes.
- [func moveChildCollections(at: IndexSet, to: Int)](./movechildcollections%28at,to%29.md)
  Moves the child collections at the specified indexes in the collection list to a new index.
- [func replaceChildCollections(at: IndexSet, withChildCollections: any NSFastEnumeration)](./replacechildcollections%28at,withchildcollections%29.md)
  Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [func removeChildCollections(any NSFastEnumeration)](./removechildcollections%28_%29.md)
  Removes the specified child collections from the collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/removechildcollections(at:))*