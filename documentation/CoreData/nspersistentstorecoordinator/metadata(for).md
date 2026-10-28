# metadata(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the metadata of the specified persistent store.

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
func metadata(for store: NSPersistentStore) -> [String : Any]
```

```objc
- (NSDictionary<NSString *,id> *) metadataForPersistentStore:(NSPersistentStore *) store;
```

## Return Value

A dictionary that contains the metadata currently stored or to-be-stored in `store`.

## Parameters

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
- [func setMetadata([String : Any]?, for: NSPersistentStore)](./setmetadata%28_,for%29.md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](../nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](../nsstoreuuidkey.md)
  A key that provides the store’s UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadata(for:))*