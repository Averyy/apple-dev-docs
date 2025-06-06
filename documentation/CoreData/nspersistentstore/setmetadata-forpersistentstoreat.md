# setMetadata(_:forPersistentStoreAt:)

**Framework**: Core Data  
**Kind**: method

Sets the metadata for the store at a given URL.

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
class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreAt url: URL) throws
```

#### Discussion

Subclasses must override this method to set metadata appropriately.

## Parameters

- `metadata`: The metadata for the store at  .
- `url`: The location of the store.

## See Also

- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](nspersistentstore/metadataforpersistentstore(with:).md)
  Returns the metadata from the persistent store at the given URL.
- [func loadMetadata() throws](nspersistentstore/loadmetadata.md)
  Instructs the persistent store to load its metadata.
- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/setmetadata(_:forpersistentstoreat:))*