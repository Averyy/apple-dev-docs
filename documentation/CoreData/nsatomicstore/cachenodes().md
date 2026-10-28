# cacheNodes()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the set of cache nodes registered with the receiver.

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
func cacheNodes() -> Set<NSAtomicStoreCacheNode>
```

```objc
- (NSSet<__kindof NSAtomicStoreCacheNode *> *) cacheNodes;
```

## Return Value

The set of cache nodes registered with the receiver.

## Discussion

You should modify this collection using [`addCacheNodes(_:)`](./addcachenodes%28_%29.md): and [`willRemoveCacheNodes(_:)`](./willremovecachenodes%28_%29.md).

## See Also

### Utility Methods
- [func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?](./cachenode%28for%29.md)
  Returns the cache node for a given managed object ID.
- [func referenceObject(for: NSManagedObjectID) -> Any](./referenceobject%28for%29.md)
  Returns the reference object for a given managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/cachenodes())*