# metadataForPersistentStore(with:)

**Framework**: Core Data  
**Kind**: method

Returns the metadata from the persistent store at the given URL.

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
class func metadataForPersistentStore(with url: URL) throws -> [String : Any]
```

#### Return Value

The metadata from the persistent store at `url`. Returns `nil` if there is an error.

#### Discussion

Subclasses must override this method.

## Parameters

- `url`: The location of the store.

## See Also

- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)
  Sets the metadata for the store at a given URL.
- [func loadMetadata() throws](nspersistentstore/loadmetadata.md)
  Instructs the persistent store to load its metadata.
- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/metadataforpersistentstore(with:))*