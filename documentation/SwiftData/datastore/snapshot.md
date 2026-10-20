# Snapshot

**Framework**: SwiftData  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

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
associatedtype Snapshot : DataStoreSnapshot
```

## See Also

### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](./fetch%28_%29.md)
- [struct DataStoreFetchRequest](../datastorefetchrequest.md)
- [struct DataStoreFetchResult](../datastorefetchresult.md)
- [protocol DataStoreSnapshot](../datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](../datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./fetchcount%28_%29.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/snapshot)*