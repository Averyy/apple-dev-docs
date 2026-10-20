# addPersistentStore(with:completionHandler:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addPersistentStoreWithDescription:(NSPersistentStoreDescription *) storeDescription completionHandler:(void (^)(NSPersistentStoreDescription *, NSError *)) block;
```

## Parameters

- `storeDescription`: A description object used to create and load a persistent store.
- `block`: The completion handler block that’s invoked after the store is added.

## See Also

### Adding or removing a store
- [func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String?, at: URL, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28type,configuration,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func remove(NSPersistentStore) throws](./remove%28_%29.md)
  Removes the specified persistent store from the coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(with:completionhandler:))*