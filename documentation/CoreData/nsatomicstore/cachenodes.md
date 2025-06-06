# cacheNodes()

**Framework**: Core Data  
**Kind**: method

Returns the set of cache nodes registered with the receiver.

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
func cacheNodes() -> Set<NSAtomicStoreCacheNode>
```

#### Return Value

The set of cache nodes registered with the receiver.

#### Discussion

You should modify this collection using [`addCacheNodes(_:)`](nsatomicstore/addcachenodes(_:).md): and [`willRemoveCacheNodes(_:)`](nsatomicstore/willremovecachenodes(_:).md).

## See Also

- [func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?](nsatomicstore/cachenode(for:).md)
  Returns the cache node for a given managed object ID.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsatomicstore/referenceobject(for:).md)
  Returns the reference object for a given managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/cachenodes())*