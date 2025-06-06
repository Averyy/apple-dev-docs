# removeUbiquitousContentAndPersistentStore(at:options:)

**Framework**: Core Data  
**Kind**: method

Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
class func removeUbiquitousContentAndPersistentStore(at storeURL: URL, options: [AnyHashable : Any]? = nil) throws
```

#### Discussion

Errors may be returned as a result of file I/O, iCloud network or iCloud account issues.

## Parameters

- `storeURL`: The URL of the store to delete.
- `options`: A dictionary containing the options normally passed to  .

## See Also

- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](nspersistentstorecoordinator/elementsderived(fromexternalrecordat:).md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](nspersistentstorecoordinator/metadataforpersistentstore(with:).md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:).md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:).md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:))*