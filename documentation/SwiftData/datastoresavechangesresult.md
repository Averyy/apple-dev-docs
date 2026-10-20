# DataStoreSaveChangesResult

**Framework**: SwiftData  
**Kind**: class  
**Role**: Class

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
final class DataStoreSaveChangesResult<T> where T : DataStoreSnapshot
```

## Topics

### Initializers
- [init(for: String, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier], snapshotsToReregister: [PersistentIdentifier : T])](./datastoresavechangesresult/init%28for,remappedidentifiers,snapshotstoreregister%29.md)
- [init(for: String, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier], snapshotsToReregister: [PersistentIdentifier : T], historyToken: (any HistoryToken)?)](./datastoresavechangesresult/init%28for,remappedidentifiers,snapshotstoreregister,historytoken%29.md)
### Instance Properties
- [let historyToken: (any HistoryToken)?](./datastoresavechangesresult/historytoken.md)
- [let remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier]](./datastoresavechangesresult/remappedidentifiers.md)
- [let snapshotsToReregister: [PersistentIdentifier : T]](./datastoresavechangesresult/snapshotstoreregister.md)
- [let storeIdentifier: String](./datastoresavechangesresult/storeidentifier.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Persisting model data
- [func save(DataStoreSaveChangesRequest<Self.Snapshot>) throws -> DataStoreSaveChangesResult<Self.Snapshot>](./datastore/save%28_%29.md)
- [struct DataStoreSaveChangesRequest](./datastoresavechangesrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresavechangesresult)*