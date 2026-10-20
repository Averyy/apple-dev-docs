# NSStoreTypeKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A key that identifies the store type.

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
let NSStoreTypeKey: String
```

```c
extern NSString * const NSStoreTypeKey;
```

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
- [let NSStoreUUIDKey: String](./nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsstoretypekey)*