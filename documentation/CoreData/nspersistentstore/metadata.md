# metadata

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The metadata for the persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var metadata: [String : Any]! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) NSDictionary<NSString *,id> * metadata;
```

## Discussion

The dictionary must include the store type ([`NSStoreTypeKey`](../nsstoretypekey.md)) and UUID ([`NSStoreUUIDKey`](../nsstoreuuidkey.md)).

### Special Considerations

Subclasses must override this property to provide storage and persistence for the store metadata.

## See Also

### Managing Store Metadata
- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](./metadataforpersistentstore%28with%29.md)
  Returns the metadata from the persistent store at the given URL.
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](./setmetadata%28_,forpersistentstoreat%29.md)
  Sets the metadata for the store at a given URL.
- [func loadMetadata() throws](./loadmetadata%28%29.md)
  Instructs the persistent store to load its metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/metadata)*