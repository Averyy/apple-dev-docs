# NSStoreUUIDKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A key that provides the store’s UUID.

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
let NSStoreUUIDKey: String
```

```c
extern NSString * const NSStoreUUIDKey;
```

#### Discussion

The store UUID is useful to identify stores through URI representations, but it is *not* guaranteed to be unique. The UUID generated for new stores is unique—users can freely copy files and thus the UUID stored inside—so if you track or reference stores explicitly you need to be aware of duplicate UUIDs and potentially override the UUID when a new store is added to the list of known stores in your application.

## See Also

### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](./nspersistentstorecoordinator/setmetadata%28_,type,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./nspersistentstorecoordinator/metadataforpersistentstore%28type,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./nspersistentstorecoordinator/setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./nspersistentstorecoordinator/metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](./nspersistentstorecoordinator/metadata%28for%29.md)
  Returns the metadata of the specified persistent store.
- [func setMetadata([String : Any]?, for: NSPersistentStore)](./nspersistentstorecoordinator/setmetadata%28_,for%29.md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](./nsstoretypekey.md)
  A key that identifies the store type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsstoreuuidkey)*