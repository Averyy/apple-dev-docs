# referenceObject(for:)

**Framework**: Core Data  
**Kind**: method

Returns the reference object for a given managed object ID.

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
func referenceObject(for objectID: NSManagedObjectID) -> Any
```

#### Return Value

The reference object for `objectID`.

#### Discussion

Subclasses should invoke this method to extract the reference data from the object ID for each cache node if the data is to be made persistent.

## Parameters

- `objectID`: A managed object ID.

## See Also

- [func cacheNodes() -> Set<NSAtomicStoreCacheNode>](nsatomicstore/cachenodes.md)
  Returns the set of cache nodes registered with the receiver.
- [func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?](nsatomicstore/cachenode(for:).md)
  Returns the cache node for a given managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/referenceobject(for:))*