# cacheNode(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the cache node for a given managed object ID.

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
func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?
```

```objc
- (NSAtomicStoreCacheNode *) cacheNodeForObjectID:(NSManagedObjectID *) objectID;
```

## Return Value

The cache node for `objectID`.

## Discussion

This method is normally used by cache nodes to locate related cache nodes (by relationships).

## Parameters

- `objectID`: A managed object ID.

## See Also

### Utility Methods
- [func cacheNodes() -> Set<NSAtomicStoreCacheNode>](./cachenodes%28%29.md)
  Returns the set of cache nodes registered with the receiver.
- [func referenceObject(for: NSManagedObjectID) -> Any](./referenceobject%28for%29.md)
  Returns the reference object for a given managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/cachenode(for:))*