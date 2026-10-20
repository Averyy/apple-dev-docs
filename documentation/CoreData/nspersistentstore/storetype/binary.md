# binary

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A store that reads from and writes to a persistent binary file.

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
static let binary: NSPersistentStore.StoreType
```

#### Discussion

A binary store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [`sqlite`](./sqlite.md) store, which you can partially modify.

## See Also

### Store Types
- [static let inMemory: NSPersistentStore.StoreType](./inmemory.md)
  An ephemeral store that reads from and writes to memory only.
- [static let sqlite: NSPersistentStore.StoreType](./sqlite.md)
  A store that reads from and writes to a persistent SQLite database.
- [static let xml: NSPersistentStore.StoreType](./xml.md)
  A store that reads from and writes to a persistent XML file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/binary)*