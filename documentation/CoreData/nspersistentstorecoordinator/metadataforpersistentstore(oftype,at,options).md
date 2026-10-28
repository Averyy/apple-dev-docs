# metadataForPersistentStore(ofType:at:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns the metadata of a specific type of persistent store at the provided location.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`metadataForPersistentStore(type:at:options:)`](./metadataforpersistentstore%28type,at,options%29.md) instead.

## Declaration

```swift
class func metadataForPersistentStore(ofType storeType: String, at url: URL, options: [AnyHashable : Any]? = nil) throws -> [String : Any]
```

```objc
+ (NSDictionary<NSString *,id> *) metadataForPersistentStoreOfType:(NSString *) storeType URL:(NSURL *) url options:(NSDictionary *) options error:(NSError **) error;
```

## Return Value

A dictionary that contains, at a minimum, values for the [`NSStoreTypeKey`](../nsstoretypekey.md) and [`NSStoreUUIDKey`](../nsstoreuuidkey.md) keys.

## Parameters

- `storeType`: The type of the store. If `nil`, Core Data automatically attempts to determine the store class to use.
- `url`: The file URL of the store.
- `options`: A dictionary that contains options for the store.

## See Also

### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,type,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28type,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](./metadata%28for%29.md)
  Returns the metadata of the specified persistent store.
- [func setMetadata([String : Any]?, for: NSPersistentStore)](./setmetadata%28_,for%29.md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](../nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](../nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:))*