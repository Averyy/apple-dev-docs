# willRemoveCacheNodes(_:)

**Framework**: Core Data  
**Kind**: method

Method invoked before the store removes the given collection of cache nodes.

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
func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)
```

#### Discussion

This method is invoked by the store before the call to [`save()`](nsatomicstore/save().md) with the collection of cache nodes marked as deleted by a managed object context.  You can override this method to track the nodes which will not be made persistent in the [`save()`](nsatomicstore/save().md) method.

You should not invoke this method directly in a subclass.

## Parameters

- `cacheNodes`: The set of cache nodes to remove.

## See Also

- [func save() throws](nsatomicstore/save.md)
  Saves the cache nodes.
- [func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode](nsatomicstore/newcachenode(for:).md)
  Returns a new cache node for a given managed object.
- [func newReferenceObject(for: NSManagedObject) -> Any](nsatomicstore/newreferenceobject(for:).md)
  Returns a new reference object for a given managed object.
- [func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)](nsatomicstore/updatecachenode(_:from:).md)
  Updates the given cache node using the values in a given managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/willremovecachenodes(_:))*