# DataStoreFetchRequest

**Framework**: SwiftData  
**Kind**: struct

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
struct DataStoreFetchRequest<T> where T : PersistentModel
```

## Topics

### Instance Properties
- [let descriptor: FetchDescriptor<T>](datastorefetchrequest/descriptor.md)
- [let editingState: EditingState](datastorefetchrequest/editingstate.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](datastore/fetch(_:).md)
- [struct DataStoreFetchResult](datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](datastore/snapshot.md)
- [protocol DataStoreSnapshot](datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](datastore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](datastore/fetchidentifiers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastorefetchrequest)*