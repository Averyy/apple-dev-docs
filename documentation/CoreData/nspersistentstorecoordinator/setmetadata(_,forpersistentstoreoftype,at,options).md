# setMetadata(_:forPersistentStoreOfType:at:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Updates the metadata of a specific type of persistent store at the provided location.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`setMetadata(_:type:at:options:)`](./setmetadata%28_,type,at,options%29.md) instead.

## Declaration

```swift
class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String, at url: URL, options: [AnyHashable : Any]? = nil) throws
```

```objc
+ (BOOL) setMetadata:(NSDictionary<NSString *,id> *) metadata forPersistentStoreOfType:(NSString *) storeType URL:(NSURL *) url options:(NSDictionary *) options error:(NSError **) error;
```

## Parameters

- `metadata`: A dictionary that contains the metadata to store.
- `storeType`: The type of store. If `nil`, Core Data automatically attempts to determine the store class to use.
- `url`: The file URL of the store.
- `options`: A dictionary that contains options for the store.

## See Also

### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,type,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28type,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:))*