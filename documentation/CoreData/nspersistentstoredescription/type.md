# type

**Framework**: Core Data  
**Kind**: property

The type of store this description represents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var type: String { get set }
```

#### Discussion

A string constant (such as `NSSQLiteStoreType`) that specifies the type of the new store—see [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md).

## See Also

- [var url: URL?](nspersistentstoredescription/url.md)
  The URL that the store will use for its location.
- [var configuration: String?](nspersistentstoredescription/configuration.md)
  The name of the configuration used by this store.
- [var timeout: TimeInterval](nspersistentstoredescription/timeout.md)
  The connection timeout for the associated store.
- [var isReadOnly: Bool](nspersistentstoredescription/isreadonly.md)
  A flag that indicates whether this store will be read-only.
- [var shouldAddStoreAsynchronously: Bool](nspersistentstoredescription/shouldaddstoreasynchronously.md)
  A flag that determines whether the store is added asynchronously.
- [var shouldInferMappingModelAutomatically: Bool](nspersistentstoredescription/shouldinfermappingmodelautomatically.md)
  A flag indicating whether a mapping model should be created automatically.
- [var shouldMigrateStoreAutomatically: Bool](nspersistentstoredescription/shouldmigratestoreautomatically.md)
  A flag indicating whether the associated persistent store should be migrated automatically.
- [func setOption(NSObject?, forKey: String)](nspersistentstoredescription/setoption(_:forkey:).md)
  Sets an option on the store.
- [func setValue(NSObject?, forPragmaNamed: String)](nspersistentstoredescription/setvalue(_:forpragmanamed:).md)
  Allows you to set pragmas for the SQLite store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/type)*