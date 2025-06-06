# DefaultStore

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
final class DefaultStore
```

## Topics

### Initializers
- [convenience init(ModelConfiguration, migrationPlan: (any SchemaMigrationPlan.Type)?) throws](defaultstore/init(_:migrationplan:).md)
### Instance Properties
- [let configuration: ModelConfiguration](defaultstore/configuration-swift.property.md)
- [var identifier: String](defaultstore/identifier.md)
- [let name: String](defaultstore/name.md)
- [let schema: Schema](defaultstore/schema.md)
### Instance Methods
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : DefaultStore.Snapshot]](defaultstore/cachedsnapshots(for:editingstate:).md)
- [func delete<T>(DataStoreBatchDeleteRequest<T>) throws](defaultstore/delete(_:).md)
- [func erase() throws](defaultstore/erase.md)
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, DefaultStore.Snapshot>](defaultstore/fetch(_:).md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](defaultstore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](defaultstore/fetchidentifiers(_:).md)
- [func initializeState(for: EditingState)](defaultstore/initializestate(for:).md)
- [func invalidateState(for: EditingState)](defaultstore/invalidatestate(for:).md)
- [func save(DataStoreSaveChangesRequest<DefaultStore.Snapshot>) throws -> DataStoreSaveChangesResult<DefaultStore.Snapshot>](defaultstore/save(_:).md)
### Type Aliases
- [DefaultStore.Configuration](defaultstore/configuration-swift.typealias.md)
- [DefaultStore.Snapshot](defaultstore/snapshot.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore)*