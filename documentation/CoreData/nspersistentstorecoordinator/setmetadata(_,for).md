# setMetadata(_:for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Updates the metadata for the specified persistent store.

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
func setMetadata(_ metadata: [String : Any]?, for store: NSPersistentStore)
```

```objc
- (void) setMetadata:(NSDictionary<NSString *,id> *) metadata forPersistentStore:(NSPersistentStore *) store;
```

#### Discussion

The store type and UUID (`NSStoreTypeKey` and `NSStoreUUIDKey`) are always added automatically, however `NSStoreUUIDKey` is only added if it is not set manually as part of the dictionary argument.

> ❗ **Important**:  Setting the metadata for a store does not change the information on disk until the store is actually saved.

## Parameters

- `metadata`: A dictionary containing metadata for the store.
- `store`: A persistent store.

## See Also

### Related Documentation
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](./setmetadata%28_,forpersistentstoreoftype,at%29.md)
  Sets the metadata for a given store.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at%29.md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,type,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28type,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](./metadata%28for%29.md)
  Returns the metadata of the specified persistent store.
- [let NSStoreTypeKey: String](../nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](../nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:for:))*