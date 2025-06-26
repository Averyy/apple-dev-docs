# fetchCount(_:)

**Framework**: SwiftData  
**Kind**: method  
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
func fetchCount<T>(_ request: DataStoreFetchRequest<T>) throws -> Int where T : PersistentModel
```

## See Also

- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](datastore/fetch(_:).md)
- [struct DataStoreFetchRequest](datastorefetchrequest.md)
- [struct DataStoreFetchResult](datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](datastore/snapshot.md)
- [protocol DataStoreSnapshot](datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](datastore/fetchidentifiers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/fetchcount(_:))*