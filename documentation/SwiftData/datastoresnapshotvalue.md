# DataStoreSnapshotValue

**Framework**: SwiftData  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
typealias DataStoreSnapshotValue = Codable & Sendable
```

## See Also

### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](./datastore/fetch%28_%29.md)
- [struct DataStoreFetchRequest](./datastorefetchrequest.md)
- [struct DataStoreFetchResult](./datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](./datastore/snapshot.md)
- [protocol DataStoreSnapshot](./datastoresnapshot.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./datastore/fetchcount%28_%29.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./datastore/fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresnapshotvalue)*