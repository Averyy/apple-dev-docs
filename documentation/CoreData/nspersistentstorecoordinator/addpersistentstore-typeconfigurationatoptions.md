# addPersistentStore(type:configuration:at:options:)

**Framework**: Core Data  
**Kind**: method

Adds a specific type of persistent store at the provided location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String? = nil, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore
```

## Parameters

- `type`: The store type. For possible values, see  .
- `configuration`: The name of the configuration to use. You must define this configuration in the coordinator’s managed object model.
- `storeURL`: The store’s location.
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see  .

## See Also

- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(with: NSPersistentStoreDescription, completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](nspersistentstorecoordinator/addpersistentstore(with:completionhandler:).md)
  Adds a persistent store using the provided description.
- [func remove(NSPersistentStore) throws](nspersistentstorecoordinator/remove(_:).md)
  Removes the specified persistent store from the coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(type:configuration:at:options:))*