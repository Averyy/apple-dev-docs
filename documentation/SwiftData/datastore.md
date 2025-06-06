# DataStore

**Framework**: SwiftData  
**Kind**: protocol

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

### Associated Types
- [associatedtype Configuration : DataStoreConfiguration](datastore/configuration-swift.associatedtype.md)
- [associatedtype Snapshot : DataStoreSnapshot](datastore/snapshot.md)
### Initializers
- [init(Self.Configuration, migrationPlan: (any SchemaMigrationPlan.Type)?) throws](datastore/init(_:migrationplan:).md)
### Instance Properties
- [var configuration: Self.Configuration](datastore/configuration-swift.property.md)
- [var identifier: String](datastore/identifier.md)
- [var schema: Schema](datastore/schema.md)
### Instance Methods
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : Self.Snapshot]](datastore/cachedsnapshots(for:editingstate:).md)
- [func erase() throws](datastore/erase.md)
- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, Self.Snapshot>](datastore/fetch(_:).md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](datastore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](datastore/fetchidentifiers(_:).md)
- [func initializeState(for: EditingState)](datastore/initializestate(for:).md)
- [func invalidateState(for: EditingState)](datastore/invalidatestate(for:).md)
- [func save(DataStoreSaveChangesRequest<Self.Snapshot>) throws -> DataStoreSaveChangesResult<Self.Snapshot>](datastore/save(_:).md)

## Relationships

### Inherited By
- [DataStoreBatching](datastorebatching.md)
### Conforming Types
- [DefaultStore](defaultstore.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore)*