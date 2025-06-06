# elementsDerived(fromExternalRecordAt:)

**Framework**: Core Data  
**Kind**: method

Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func elementsDerived(fromExternalRecordAt fileURL: URL) -> [AnyHashable : Any]
```

#### Return Value

A dictionary containing the parsed elements derived from the Spotlight support file specified by `fileURL`.

#### Discussion

Dictionary keys and the corresponding values are described in [`Spotlight record keys`](spotlight-record-keys.md).

## Parameters

- `fileURL`: A file URL specifying the location of a Spotlight external record file.

## See Also

- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](nspersistentstorecoordinator/metadataforpersistentstore(with:).md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:).md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func removeUbiquitousContentAndPersistentStore(at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:).md)
  Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:).md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/elementsderived(fromexternalrecordat:))*