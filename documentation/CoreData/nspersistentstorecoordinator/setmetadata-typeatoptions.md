# setMetadata(_:type:at:options:)

**Framework**: Core Data  
**Kind**: method

Updates the metadata of a specific type of persistent store at the provided location.

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
class func setMetadata(_ metadata: [String : Any]?, type storeType: NSPersistentStore.StoreType, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `metadata`: A dictionary that contains the metadata to associate with the store.
- `storeType`: The store type. For possible values, see  .
- `storeURL`: The store’s location.
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see  .

## See Also

- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(type:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](nspersistentstorecoordinator/metadata(for:).md)
  Returns the metadata of the specified persistent store.
- [func setMetadata([String : Any]?, for: NSPersistentStore)](nspersistentstorecoordinator/setmetadata(_:for:).md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:type:at:options:))*