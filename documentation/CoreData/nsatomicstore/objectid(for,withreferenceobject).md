# objectID(for:withReferenceObject:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a managed object ID from the reference data for a specified entity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objectID(for entity: NSEntityDescription, withReferenceObject data: Any) -> NSManagedObjectID
```

```objc
- (NSManagedObjectID *) objectIDForEntity:(NSEntityDescription *) entity referenceObject:(id) data;
```

## Return Value

The managed object ID from the reference data for a specified entity

## Discussion

You use this method to create managed object IDs which are then used to create cache nodes for information being loaded into the store.

### Special Considerations

You should not override this method.

## Parameters

- `entity`: An entity description object.
- `data`: Reference data for which the managed object ID is required.

## See Also

### Loading a Store
- [func load() throws](./load%28%29.md)
  Loads the cache nodes for the receiver.
- [func addCacheNodes(Set<NSAtomicStoreCacheNode>)](./addcachenodes%28_%29.md)
  Registers a set of cache nodes with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/objectid(for:withreferenceobject:))*