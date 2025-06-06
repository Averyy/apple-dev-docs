# load()

**Framework**: Core Data  
**Kind**: method

Loads the cache nodes for the receiver.

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
func load() throws
```

#### Discussion

You override this method to load the data from the URL specified in [`init(persistentStoreCoordinator:configurationName:at:options:)`](nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:).md) and create cache nodes for the represented objects. You must respect the configuration specified for the store, as well as the options.

Any subclass of `NSAtomicStore` must be able to handle being initialized with a URL pointing to a zero-length file. This serves as an indicator that a new store is to be constructed at the specified location and allows you to securely create reservation files in known locations which can then be passed to Core Data to construct stores. You may choose to create zero-length reservation files during [`init(persistentStoreCoordinator:configurationName:at:options:)`](nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:).md) or [`load()`](nsatomicstore/load().md). If you do so, you must remove the reservation file if the store is removed from the coordinator before it is saved.

You must override this method in a subclass of `NSAtomicStore`.

## See Also

- [func objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](nsatomicstore/objectid(for:withreferenceobject:).md)
  Returns a managed object ID from the reference data for a specified entity.
- [func addCacheNodes(Set<NSAtomicStoreCacheNode>)](nsatomicstore/addcachenodes(_:).md)
  Registers a set of cache nodes with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/load())*