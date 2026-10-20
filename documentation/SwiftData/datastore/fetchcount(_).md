# fetchCount(_:)

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
func fetchCount<T>(_ request: DataStoreFetchRequest<T>) throws -> Int where T : PersistentModel
```

## Default Implementations

### DataStore Implementations
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./fetchcount%28_%29-91yf3.md)

## See Also

### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](./fetch%28_%29.md)
- [struct DataStoreFetchRequest](../datastorefetchrequest.md)
- [struct DataStoreFetchResult](../datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](./snapshot.md)
- [protocol DataStoreSnapshot](../datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](../datastoresnapshotvalue.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/fetchcount(_:))*