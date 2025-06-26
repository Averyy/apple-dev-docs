# DefaultStore

**Framework**: SwiftData  
**Kind**: class

A data store that uses Core Data as its undelying storage mechanism.

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
final class DefaultStore
```

## Topics

### Creating a data store
- [convenience init(ModelConfiguration, migrationPlan: (any SchemaMigrationPlan.Type)?) throws](defaultstore/init(_:migrationplan:).md)
### Accessing store information
- [let configuration: ModelConfiguration](defaultstore/configuration-swift.property.md)
- [DefaultStore.Configuration](defaultstore/configuration-swift.typealias.md)
- [var identifier: String](defaultstore/identifier.md)
- [let name: String](defaultstore/name.md)
- [let schema: Schema](defaultstore/schema.md)
### Processing fetch requests
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, DefaultStore.Snapshot>](defaultstore/fetch(_:).md)
- [DefaultStore.Snapshot](defaultstore/snapshot.md)
- [struct DefaultSnapshot](defaultsnapshot.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](defaultstore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](defaultstore/fetchidentifiers(_:).md)
### Persisting model data
- [func save(DataStoreSaveChangesRequest<DefaultStore.Snapshot>) throws -> DataStoreSaveChangesResult<DefaultStore.Snapshot>](defaultstore/save(_:).md)
### Deleting persisted model data
- [func delete<T>(DataStoreBatchDeleteRequest<T>) throws](defaultstore/delete(_:).md)
- [func erase() throws](defaultstore/erase.md)
### Sharing cached data between model contexts
- [func initializeState(for: EditingState)](defaultstore/initializestate(for:).md)
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : DefaultStore.Snapshot]](defaultstore/cachedsnapshots(for:editingstate:).md)
- [func invalidateState(for: EditingState)](defaultstore/invalidatestate(for:).md)
### Managing model change history
- [func fetchHistory(HistoryDescriptor<DefaultHistoryTransaction>) throws -> [DefaultHistoryTransaction]](defaultstore/fetchhistory(_:).md)
- [func deleteHistory(HistoryDescriptor<DefaultHistoryTransaction>) throws](defaultstore/deletehistory(_:).md)
- [DefaultStore.HistoryType](defaultstore/historytype-swift.typealias.md)
- [DefaultStore.TokenType](defaultstore/tokentype.md)
### Default Implementations
- [DataStore Implementations](defaultstore/datastore-implementations.md)
- [HistoryProviding Implementations](defaultstore/historyproviding-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DataStore](datastore.md)
- [DataStoreBatching](datastorebatching.md)
- [HistoryProviding](historyproviding.md)

## See Also

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [protocol DataStore](datastore.md)
  An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [protocol DataStoreBatching](datastorebatching.md)
  An interface that enables a custom data store to support batch requests.
- [protocol HistoryProviding](historyproviding.md)
  An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct ModelDocument](modeldocument.md)
  A document type that uses SwiftData to manage its storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore)*