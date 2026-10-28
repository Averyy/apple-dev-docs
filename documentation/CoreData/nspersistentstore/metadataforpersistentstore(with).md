# metadataForPersistentStore(with:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns the metadata from the persistent store at the given URL.

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
class func metadataForPersistentStore(with url: URL) throws -> [String : Any]
```

```objc
+ (NSDictionary<NSString *,id> *) metadataForPersistentStoreWithURL:(NSURL *) url error:(NSError **) error;
```

## Return Value

The metadata from the persistent store at `url`. Returns `nil` if there is an error.

## Discussion

Subclasses must override this method.

## Parameters

- `url`: The location of the store.

## See Also

### Managing Store Metadata
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](./setmetadata%28_,forpersistentstoreat%29.md)
  Sets the metadata for the store at a given URL.
- [func loadMetadata() throws](./loadmetadata%28%29.md)
  Instructs the persistent store to load its metadata.
- [var metadata: [String : Any]!](./metadata.md)
  The metadata for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/metadataforpersistentstore(with:))*