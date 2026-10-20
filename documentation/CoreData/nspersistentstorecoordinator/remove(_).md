# remove(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Removes the specified persistent store from the coordinator.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remove(_ store: NSPersistentStore) throws
```

```objc
- (BOOL) removePersistentStore:(NSPersistentStore *) store error:(NSError **) error;
```

## Parameters

- `store`: A persistent store.

## See Also

### Related Documentation
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
### Adding or removing a store
- [func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String?, at: URL, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28type,configuration,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(with: NSPersistentStoreDescription, completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](./addpersistentstore%28with,completionhandler%29.md)
  Adds a persistent store using the provided description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/remove(_:))*