# updateCacheNode(_:from:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Updates the given cache node using the values in a given managed object.

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
func updateCacheNode(_ node: NSAtomicStoreCacheNode, from managedObject: NSManagedObject)
```

```objc
- (void) updateCacheNode:(NSAtomicStoreCacheNode *) node fromManagedObject:(NSManagedObject *) managedObject;
```

#### Discussion

This method is invoked by the framework after a save operation on a managed object context, once for each updated `NSManagedObject` instance.

You override this method in a subclass to take the information from `managedObject` and update `node`.

##### Special Considerations

You must override this method.

## Parameters

- `node`: The cache node to update.
- `managedObject`: The managed object with which to update `node`.

## See Also

### Updating Cache Nodes
- [func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode](./newcachenode%28for%29.md)
  Returns a new cache node for a given managed object.
- [func newReferenceObject(for: NSManagedObject) -> Any](./newreferenceobject%28for%29.md)
  Returns a new reference object for a given managed object.
- [func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)](./willremovecachenodes%28_%29.md)
  Method invoked before the store removes the given collection of cache nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/updatecachenode(_:from:))*