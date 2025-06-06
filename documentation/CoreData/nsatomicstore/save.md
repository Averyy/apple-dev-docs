# save()

**Framework**: Core Data  
**Kind**: method

Saves the cache nodes.

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
func save() throws
```

#### Discussion

You override this method to make persistent the necessary information from the cache nodes to the URL specified for the receiver.

##### Special Considerations

You must override this method.

## See Also

- [func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)](nsatomicstore/updatecachenode(_:from:).md)
  Updates the given cache node using the values in a given managed object.
- [func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)](nsatomicstore/willremovecachenodes(_:).md)
  Method invoked before the store removes the given collection of cache nodes.
- [func newReferenceObject(for: NSManagedObject) -> Any](nsatomicstore/newreferenceobject(for:).md)
  Returns a new reference object for a given managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/save())*