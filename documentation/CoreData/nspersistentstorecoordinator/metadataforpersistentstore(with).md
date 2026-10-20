# metadataForPersistentStore(with:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns a dictionary that contains the metadata stored in the persistent store at the specified location.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`metadataForPersistentStore(ofType:at:)`](./metadataforpersistentstore%28oftype,at%29.md) instead.

## Declaration

```swift
class func metadataForPersistentStore(with url: URL) throws -> [AnyHashable : Any]
```

```objc
+ (NSDictionary *) metadataForPersistentStoreWithURL:(NSURL *) url error:(NSError **) error;
```

#### Return Value

A dictionary containing the metadata for the persistent store at `url`. If no store is found, or there is a problem accessing its contents, returns `nil`. The keys guaranteed to be in this dictionary are `NSStoreTypeKey` and `NSStoreUUIDKey`.

#### Discussion

This method allows you to access the metadata in a persistent store without initializing a Core Data stack.

## Parameters

- `url`: An URL object that specifies the location of a persistent store.

## See Also

### Related Documentation
- [func setMetadata([String : Any]?, for: NSPersistentStore)](./setmetadata%28_,for%29.md)
  Updates the metadata for the specified persistent store.
- [func metadata(for: NSPersistentStore) -> [String : Any]](./metadata%28for%29.md)
  Returns the metadata of the specified persistent store.
### Deprecated type methods
- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](./elementsderived%28fromexternalrecordat%29.md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at%29.md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](./registerstoreclass%28_,forstoretype%29.md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func removeUbiquitousContentAndPersistentStore(at: URL, options: [AnyHashable : Any]?) throws](./removeubiquitouscontentandpersistentstore%28at,options%29.md)
  Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](./setmetadata%28_,forpersistentstoreoftype,at%29.md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(with:))*