# loadMetadata()

**Framework**: Core Data  
**Kind**: method

Instructs the persistent store to load its metadata.

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
func loadMetadata() throws
```

#### Discussion

There is no way to return an error if the store is invalid.

## See Also

- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](nspersistentstore/metadataforpersistentstore(with:).md)
  Returns the metadata from the persistent store at the given URL.
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)
  Sets the metadata for the store at a given URL.
- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/loadmetadata())*