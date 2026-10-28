# xml

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A store that reads from and writes to a persistent XML file.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static let xml: NSPersistentStore.StoreType
```

## Discussion

An XML store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [`sqlite`](./sqlite.md) store, which you can partially modify.

## See Also

### Store Types
- [static let binary: NSPersistentStore.StoreType](./binary.md)
  A store that reads from and writes to a persistent binary file.
- [static let inMemory: NSPersistentStore.StoreType](./inmemory.md)
  An ephemeral store that reads from and writes to memory only.
- [static let sqlite: NSPersistentStore.StoreType](./sqlite.md)
  A store that reads from and writes to a persistent SQLite database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/xml)*