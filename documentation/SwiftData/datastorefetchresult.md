# DataStoreFetchResult

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

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
struct DataStoreFetchResult<ModelType, SnapshotType> where ModelType : PersistentModel, SnapshotType : DataStoreSnapshot
```

## Topics

### Initializers
- [init(descriptor: FetchDescriptor<ModelType>, fetchedSnapshots: [SnapshotType], relatedSnapshots: [PersistentIdentifier : SnapshotType])](./datastorefetchresult/init%28descriptor,fetchedsnapshots,relatedsnapshots%29.md)
### Instance Properties
- [let descriptor: FetchDescriptor<ModelType>](./datastorefetchresult/descriptor.md)
- [let fetchedSnapshots: [SnapshotType]](./datastorefetchresult/fetchedsnapshots.md)
- [let relatedSnapshots: [PersistentIdentifier : SnapshotType]](./datastorefetchresult/relatedsnapshots.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](./datastore/fetch%28_%29.md)
- [struct DataStoreFetchRequest](./datastorefetchrequest.md)
- [associatedtype Snapshot : DataStoreSnapshot](./datastore/snapshot.md)
- [protocol DataStoreSnapshot](./datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](./datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./datastore/fetchcount%28_%29.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./datastore/fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastorefetchresult)*