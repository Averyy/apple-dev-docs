# fetch(_:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method  
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
func fetch<T>(_ request: DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot> where T : PersistentModel
```

## See Also

### Processing fetch requests
- [struct DataStoreFetchRequest](../datastorefetchrequest.md)
- [struct DataStoreFetchResult](../datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](./snapshot.md)
- [protocol DataStoreSnapshot](../datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](../datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./fetchcount%28_%29.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/fetch(_:))*