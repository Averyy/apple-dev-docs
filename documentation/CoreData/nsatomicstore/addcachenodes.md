# addCacheNodes(_:)

**Framework**: Core Data  
**Kind**: method

Registers a set of cache nodes with the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)
```

#### Discussion

You should invoke this method in a subclass during the call to [`load()`](nsatomicstore/load().md) to register the loaded information with the store.

## Parameters

- `cacheNodes`: A set of cache nodes.

## See Also

- [func load() throws](nsatomicstore/load.md)
  Loads the cache nodes for the receiver.
- [func objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](nsatomicstore/objectid(for:withreferenceobject:).md)
  Returns a managed object ID from the reference data for a specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/addcachenodes(_:))*