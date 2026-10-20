# metadataForPersistentStore(type:at:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns the metadata of a specific type of persistent store at the provided location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
class func metadataForPersistentStore(type storeType: NSPersistentStore.StoreType, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws -> [String : Any]
```

## Parameters

- `storeType`: The store type. For possible values, see [`NSPersistentStore.StoreType`](../nspersistentstore/storetype.md).
- `storeURL`: The store’s location.
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,type,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](./metadata%28for%29.md)
  Returns the metadata of the specified persistent store.
- [func setMetadata([String : Any]?, for: NSPersistentStore)](./setmetadata%28_,for%29.md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](../nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](../nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(type:at:options:))*