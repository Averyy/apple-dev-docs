# cacheNode(for:)

**Framework**: Core Data  
**Kind**: method

Returns the cache node for a given managed object ID.

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
func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?
```

#### Return Value

The cache node for `objectID`.

#### Discussion

This method is normally used by cache nodes to locate related cache nodes (by relationships).

## Parameters

- `objectID`: A managed object ID.

## See Also

- [func cacheNodes() -> Set<NSAtomicStoreCacheNode>](nsatomicstore/cachenodes.md)
  Returns the set of cache nodes registered with the receiver.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsatomicstore/referenceobject(for:).md)
  Returns the reference object for a given managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/cachenode(for:))*