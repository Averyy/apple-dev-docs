# metadata

**Framework**: Core Data  
**Kind**: property

The metadata for the persistent store.

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
var metadata: [String : Any]! { get set }
```

#### Discussion

The dictionary must include the store type ([`NSStoreTypeKey`](nsstoretypekey.md)) and UUID ([`NSStoreUUIDKey`](nsstoreuuidkey.md)).

##### Special Considerations

Subclasses must override this property to provide storage and persistence for the store metadata.

## See Also

- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](nspersistentstore/metadataforpersistentstore(with:).md)
  Returns the metadata from the persistent store at the given URL.
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)
  Sets the metadata for the store at a given URL.
- [func loadMetadata() throws](nspersistentstore/loadmetadata.md)
  Instructs the persistent store to load its metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/metadata)*