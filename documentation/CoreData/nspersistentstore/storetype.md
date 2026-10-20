# NSPersistentStore.StoreType

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

The types of persistent stores that Core Data supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
struct StoreType
```

## Topics

### Store Types
- [static let binary: NSPersistentStore.StoreType](./storetype/binary.md)
  A store that reads from and writes to a persistent binary file.
- [static let inMemory: NSPersistentStore.StoreType](./storetype/inmemory.md)
  An ephemeral store that reads from and writes to memory only.
- [static let sqlite: NSPersistentStore.StoreType](./storetype/sqlite.md)
  A store that reads from and writes to a persistent SQLite database.
- [static let xml: NSPersistentStore.StoreType](./storetype/xml.md)
  A store that reads from and writes to a persistent XML file.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Getting Store Configuration
- [var configurationName: String](./configurationname.md)
  The name of the managed object model configuration that creates the persistent store.
- [var options: [AnyHashable : Any]?](./options.md)
  The options that Core Data uses to create the store.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](./persistentstorecoordinator.md)
  The persistent store coordinator that loads the persistent store.
- [var type: String](./type.md)
  The type string of the persistent store.
- [Persistent Store Types](../persistent-store-types.md)
  Persist data through the available store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/storetype)*