# DataStoreSaveChangesResult

**Framework**: SwiftData  
**Kind**: class

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
- [init(for: String, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier], snapshotsToReregister: [PersistentIdentifier : T])](datastoresavechangesresult/init(for:remappedidentifiers:snapshotstoreregister:).md)
- [init(for: String, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier], snapshotsToReregister: [PersistentIdentifier : T], historyToken: (any HistoryToken)?)](datastoresavechangesresult/init(for:remappedidentifiers:snapshotstoreregister:historytoken:).md)
### Instance Properties
- [let historyToken: (any HistoryToken)?](datastoresavechangesresult/historytoken.md)
- [let remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier]](datastoresavechangesresult/remappedidentifiers.md)
- [let snapshotsToReregister: [PersistentIdentifier : T]](datastoresavechangesresult/snapshotstoreregister.md)
- [let storeIdentifier: String](datastoresavechangesresult/storeidentifier.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func save(DataStoreSaveChangesRequest<Self.Snapshot>) throws -> DataStoreSaveChangesResult<Self.Snapshot>](datastore/save(_:).md)
- [struct DataStoreSaveChangesRequest](datastoresavechangesrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresavechangesresult)*