# addPersistentStore(ofType:configurationName:at:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Adds a specific type of persistent store at the provided location.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`addPersistentStore(type:configuration:at:options:)`](./addpersistentstore%28type,configuration,at,options%29.md) instead.

## Declaration

```swift
func addPersistentStore(ofType storeType: String, configurationName configuration: String?, at storeURL: URL?, options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore
```

```objc
- (NSPersistentStore *) addPersistentStoreWithType:(NSString *) storeType configuration:(NSString *) configuration URL:(NSURL *) storeURL options:(NSDictionary *) options error:(NSError **) error;
```

## Mentions

- [Migrating your data model automatically](../migrating-your-data-model-automatically.md)

## Return Value

The newly created store or, if an error occurs, `nil`.

## Parameters

- `storeType`: A string constant (such as `NSSQLiteStoreType`) that specifies the store type—see [Persistent Store Types](../persistent-store-types.md) for possible values.
- `configuration`: The name of a configuration in the receiver’s managed object model that will be used by the new store. The configuration can be `nil`, in which case no other configurations are allowed.
- `storeURL`: The file location of the persistent store.
- `options`: A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see [Store options](../store-options.md) and [Migration options](../migration-options.md). This value may be `nil`.

## See Also

### Related Documentation
- [func remove(NSPersistentStore) throws](./remove%28_%29.md)
  Removes the specified persistent store from the coordinator.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt: URL, to: URL, options: [AnyHashable : Any]?, ofType: String) throws -> NSPersistentStore](./importstore%28withidentifier,fromexternalrecordsdirectoryat,to,options,oftype%29.md)
  Creates and populates a store with the external records found at a given URL.
### Adding or removing a store
- [func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String?, at: URL, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28type,configuration,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(with: NSPersistentStoreDescription, completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](./addpersistentstore%28with,completionhandler%29.md)
  Adds a persistent store using the provided description.
- [func remove(NSPersistentStore) throws](./remove%28_%29.md)
  Removes the specified persistent store from the coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:))*