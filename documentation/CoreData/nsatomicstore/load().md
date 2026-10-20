# load()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Loads the cache nodes for the receiver.

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
func load() throws
```

```objc
- (BOOL) load:(NSError **) error;
```

#### Discussion

You override this method to load the data from the URL specified in [`init(persistentStoreCoordinator:configurationName:at:options:)`](./init%28persistentstorecoordinator,configurationname,at,options%29.md) and create cache nodes for the represented objects. You must respect the configuration specified for the store, as well as the options.

Any subclass of `NSAtomicStore` must be able to handle being initialized with a URL pointing to a zero-length file. This serves as an indicator that a new store is to be constructed at the specified location and allows you to securely create reservation files in known locations which can then be passed to Core Data to construct stores. You may choose to create zero-length reservation files during [`init(persistentStoreCoordinator:configurationName:at:options:)`](./init%28persistentstorecoordinator,configurationname,at,options%29.md) or [`load()`](./load%28%29.md). If you do so, you must remove the reservation file if the store is removed from the coordinator before it is saved.

You must override this method in a subclass of `NSAtomicStore`.

## See Also

### Loading a Store
- [func objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](./objectid%28for,withreferenceobject%29.md)
  Returns a managed object ID from the reference data for a specified entity.
- [func addCacheNodes(Set<NSAtomicStoreCacheNode>)](./addcachenodes%28_%29.md)
  Registers a set of cache nodes with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/load())*