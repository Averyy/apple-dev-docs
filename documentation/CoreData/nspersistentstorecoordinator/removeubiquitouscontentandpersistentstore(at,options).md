# removeUbiquitousContentAndPersistentStore(at:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please see the release notes and Core Data documentation.

## Declaration

```swift
class func removeUbiquitousContentAndPersistentStore(at storeURL: URL, options: [AnyHashable : Any]? = nil) throws
```

```objc
+ (BOOL) removeUbiquitousContentAndPersistentStoreAtURL:(NSURL *) storeURL options:(NSDictionary *) options error:(NSError **) error;
```

#### Discussion

Errors may be returned as a result of file I/O, iCloud network or iCloud account issues.

## Parameters

- `storeURL`: The URL of the store to delete.
- `options`: A dictionary containing the options normally passed to [`addPersistentStore(ofType:configurationName:at:options:)`](./addpersistentstore%28oftype,configurationname,at,options%29.md).

## See Also

### Deprecated type methods
- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](./elementsderived%28fromexternalrecordat%29.md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](./metadataforpersistentstore%28with%29.md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at%29.md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](./registerstoreclass%28_,forstoretype%29.md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](./setmetadata%28_,forpersistentstoreoftype,at%29.md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:))*