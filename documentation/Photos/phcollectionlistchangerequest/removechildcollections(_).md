# removeChildCollections(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Removes the specified child collections from the collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func removeChildCollections(_ collections: any NSFastEnumeration)
```

```objc
- (void) removeChildCollections:(id<NSFastEnumeration>) collections;
```

## Discussion

This method removes child collections from the collection list based on their identity (determined by the [`localIdentifier`](../phobject/localidentifier.md) property of each collection). To remove objects at specified indexes, use the [`removeChildCollections(at:)`](./removechildcollections%28at%29.md) method.

## Parameters

- `collections`: An array of [`PHCollection`](../phcollection.md) objects (asset collections or other collection lists) to be removed from the collection list.

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
- [func removeChildCollections(at: IndexSet)](./removechildcollections%28at%29.md)
  Removes the child collections at the specified indexes from the collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/removechildcollections(_:))*