# DataStore

**Framework**: SwiftData  
**Kind**: protocol

An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.

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
protocol DataStore : AnyObject
```

## Topics

### Creating a data store
- [init(Self.Configuration, migrationPlan: (any SchemaMigrationPlan.Type)?) throws](datastore/init(_:migrationplan:).md)
### Accessing store information
- [var configuration: Self.Configuration](datastore/configuration-swift.property.md)
- [associatedtype Configuration : DataStoreConfiguration](datastore/configuration-swift.associatedtype.md)
- [protocol DataStoreConfiguration](datastoreconfiguration.md)
- [var identifier: String](datastore/identifier.md)
- [var schema: Schema](datastore/schema.md)
### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](datastore/fetch(_:).md)
- [struct DataStoreFetchRequest](datastorefetchrequest.md)
- [struct DataStoreFetchResult](datastorefetchresult.md)
- [associatedtype Snapshot : DataStoreSnapshot](datastore/snapshot.md)
- [protocol DataStoreSnapshot](datastoresnapshot.md)
- [typealias DataStoreSnapshotValue](datastoresnapshotvalue.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](datastore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](datastore/fetchidentifiers(_:).md)
### Persisting model data
- [func save(DataStoreSaveChangesRequest<Self.Snapshot>) throws -> DataStoreSaveChangesResult<Self.Snapshot>](datastore/save(_:).md)
- [struct DataStoreSaveChangesRequest](datastoresavechangesrequest.md)
- [class DataStoreSaveChangesResult](datastoresavechangesresult.md)
### Removing all persisted model data
- [func erase() throws](datastore/erase.md)
### Sharing cached data between model contexts
- [func initializeState(for: EditingState)](datastore/initializestate(for:).md)
- [struct EditingState](editingstate.md)
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : Self.Snapshot]](datastore/cachedsnapshots(for:editingstate:).md)
- [func invalidateState(for: EditingState)](datastore/invalidatestate(for:).md)

## Relationships

### Inherited By
- [DataStoreBatching](datastorebatching.md)
### Conforming Types
- [DefaultStore](defaultstore.md)

## See Also

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [class DefaultStore](defaultstore.md)
  A data store that uses Core Data as its undelying storage mechanism.
- [protocol DataStoreBatching](datastorebatching.md)
  An interface that enables a custom data store to support batch requests.
- [protocol HistoryProviding](historyproviding.md)
  An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct ModelDocument](modeldocument.md)
  A document type that uses SwiftData to manage its storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore)*