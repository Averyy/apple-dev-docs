# DataStoreSnapshot

**Framework**: SwiftData  
**Kind**: protocol  
**Role**: Protocol

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
protocol DataStoreSnapshot : Decodable, Encodable, Sendable
```

## Topics

### Initializers
- [init(from: any BackingData, relatedBackingDatas: inout [PersistentIdentifier : any BackingData])](./datastoresnapshot/init%28from,relatedbackingdatas%29.md)
### Instance Properties
- [var persistentIdentifier: PersistentIdentifier](./datastoresnapshot/persistentidentifier.md)
### Instance Methods
- [func copy(persistentIdentifier: PersistentIdentifier, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier]?) -> Self](./datastoresnapshot/copy%28persistentidentifier,remappedidentifiers%29.md)

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DefaultSnapshot](./defaultsnapshot.md)

## See Also

### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](./datastore/fetch%28_%29.md)
- [struct DataStoreFetchRequest](./datastorefetchrequest.md)
- [struct DataStoreFetchResult](./datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](./datastore/snapshot.md)
- [typealias DataStoreSnapshotValue](./datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](./datastore/fetchcount%28_%29.md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](./datastore/fetchidentifiers%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresnapshot)*