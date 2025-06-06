# metadataForPersistentStore(ofType:at:)

**Framework**: Core Data  
**Kind**: method

Returns a dictionary containing the metadata stored in the persistent store at a given URL.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func metadataForPersistentStore(ofType storeType: String?, at url: URL) throws -> [String : Any]
```

#### Return Value

A dictionary containing the metadata stored in the persistent store at `url`, or `nil` if the store cannot be opened or if there is a problem accessing its contents.

#### Discussion

The keys guaranteed to be in this dictionary are [`NSStoreTypeKey`](nsstoretypekey.md) and [`NSStoreUUIDKey`](nsstoreuuidkey.md).

#### Discussion

You can use this method to retrieve the metadata from a store without the overhead of creating a Core Data stack.

## Parameters

- `storeType`: The type of the store at  . If this value is  , Core Data determines which store class should be used to get or set the store file’s metadata by inspecting the file contents.
- `url`: The location of a persistent store.

## See Also

- [func setMetadata([String : Any]?, for: NSPersistentStore)](nspersistentstorecoordinator/setmetadata(_:for:).md)
  Updates the metadata for the specified persistent store.
- [func metadata(for: NSPersistentStore) -> [String : Any]](nspersistentstorecoordinator/metadata(for:).md)
  Returns the metadata of the specified persistent store.
- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](nspersistentstorecoordinator/elementsderived(fromexternalrecordat:).md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](nspersistentstorecoordinator/metadataforpersistentstore(with:).md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:))*