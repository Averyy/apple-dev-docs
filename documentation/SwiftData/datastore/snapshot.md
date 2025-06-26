# Snapshot

**Framework**: SwiftData  
**Kind**: associatedtype  
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

- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](datastore/fetch(_:).md)
- [struct DataStoreFetchRequest](datastorefetchrequest.md)
- [struct DataStoreFetchResult](datastorefetchresult.md)
- [protocol DataStoreSnapshot](datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](datastore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](datastore/fetchidentifiers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/snapshot)*