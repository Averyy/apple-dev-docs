# loadMetadata()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Instructs the persistent store to load its metadata.

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
func loadMetadata() throws
```

```objc
- (BOOL) loadMetadata:(NSError **) error;
```

#### Discussion

There is no way to return an error if the store is invalid.

## See Also

### Managing Store Metadata
- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](./metadataforpersistentstore%28with%29.md)
  Returns the metadata from the persistent store at the given URL.
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](./setmetadata%28_,forpersistentstoreat%29.md)
  Sets the metadata for the store at a given URL.
- [var metadata: [String : Any]!](./metadata.md)
  The metadata for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/loadmetadata())*