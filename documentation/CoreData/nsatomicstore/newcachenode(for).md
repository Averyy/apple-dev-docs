# newCacheNode(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a new cache node for a given managed object.

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
func newCacheNode(for managedObject: NSManagedObject) -> NSAtomicStoreCacheNode
```

```objc
- (NSAtomicStoreCacheNode *) newCacheNodeForManagedObject:(NSManagedObject *) managedObject;
```

#### Return Value

A new cache node for `managedObject`.

#### Discussion

This method is invoked by the framework during a save operation, once for each newly-inserted managed object. It should pull information from the managed object and return a cache node containing the information (the node will be registered by the framework).

##### Special Considerations

You must override this method.

## Parameters

- `managedObject`: A managed object.

## See Also

### Updating Cache Nodes
- [func newReferenceObject(for: NSManagedObject) -> Any](./newreferenceobject%28for%29.md)
  Returns a new reference object for a given managed object.
- [func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)](./updatecachenode%28_,from%29.md)
  Updates the given cache node using the values in a given managed object.
- [func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)](./willremovecachenodes%28_%29.md)
  Method invoked before the store removes the given collection of cache nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/newcachenode(for:))*