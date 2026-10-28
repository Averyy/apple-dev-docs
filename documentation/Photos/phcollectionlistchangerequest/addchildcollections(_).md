# addChildCollections(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Adds the specified collections as children of the collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addChildCollections(_ collections: any NSFastEnumeration)
```

```objc
- (void) addChildCollections:(id<NSFastEnumeration>) collections;
```

## Discussion

If you created the change request with a snapshot of the collection list’s contents using the [`init(for:childCollections:)`](./init%28for,childcollections%29.md) method, Photos inserts the new children after the existing child collections in the collection list. Otherwise, the arrangement of the new children relative to others in the collection is undefined.

## Parameters

- `collections`: An array of [`PHCollection`](../phcollection.md) objects (asset collections or other collection lists) to be added to the collection list.

## See Also

### Managing Collections
- [func insertChildCollections(any NSFastEnumeration, at: IndexSet)](./insertchildcollections%28_,at%29.md)
  Inserts the specified collections into the collection list at the specified indexes.
- [func moveChildCollections(at: IndexSet, to: Int)](./movechildcollections%28at,to%29.md)
  Moves the child collections at the specified indexes in the collection list to a new index.
- [func replaceChildCollections(at: IndexSet, withChildCollections: any NSFastEnumeration)](./replacechildcollections%28at,withchildcollections%29.md)
  Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [func removeChildCollections(any NSFastEnumeration)](./removechildcollections%28_%29.md)
  Removes the specified child collections from the collection list.
- [func removeChildCollections(at: IndexSet)](./removechildcollections%28at%29.md)
  Removes the child collections at the specified indexes from the collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/addchildcollections(_:))*