# identifierForNewStore(at:)

**Framework**: Core Data  
**Kind**: method

Returns the identifier for the store at a given URL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func identifierForNewStore(at storeURL: URL) -> Any
```

#### Return Value

The identifier for the store at `storeURL`.

## Parameters

- `storeURL`: The URL of a persistent store.

## See Also

- [func loadMetadata() throws](nsincrementalstore/loadmetadata.md)
  Loads the metadata for the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/identifierfornewstore(at:))*