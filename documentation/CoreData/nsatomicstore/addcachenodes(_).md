# addCacheNodes(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Registers a set of cache nodes with the receiver.

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
func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)
```

```objc
- (void) addCacheNodes:(NSSet<__kindof NSAtomicStoreCacheNode *> *) cacheNodes;
```

#### Discussion

You should invoke this method in a subclass during the call to [`load()`](./load%28%29.md) to register the loaded information with the store.

## Parameters

- `cacheNodes`: A set of cache nodes.

## See Also

### Loading a Store
- [func load() throws](./load%28%29.md)
  Loads the cache nodes for the receiver.
- [func objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](./objectid%28for,withreferenceobject%29.md)
  Returns a managed object ID from the reference data for a specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/addcachenodes(_:))*