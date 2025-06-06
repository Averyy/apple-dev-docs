# addPersistentStore(with:completionHandler:)

**Framework**: Core Data  
**Kind**: method

Adds a persistent store using the provided description.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func addPersistentStore(with storeDescription: NSPersistentStoreDescription, completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void)
```

## Parameters

- `storeDescription`: A description object used to create and load a persistent store.
- `block`: The completion handler block that’s invoked after the store is added.

## See Also

- [func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String?, at: URL, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(type:configuration:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func remove(NSPersistentStore) throws](nspersistentstorecoordinator/remove(_:).md)
  Removes the specified persistent store from the coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(with:completionhandler:))*