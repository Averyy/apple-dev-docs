# xml

**Framework**: Core Data  
**Kind**: property

A store that reads from and writes to a persistent XML file.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static let xml: NSPersistentStore.StoreType
```

#### Discussion

An XML store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [`sqlite`](nspersistentstore/storetype/sqlite.md) store, which you can partially modify.

## See Also

- [static let binary: NSPersistentStore.StoreType](nspersistentstore/storetype/binary.md)
  A store that reads from and writes to a persistent binary file.
- [static let inMemory: NSPersistentStore.StoreType](nspersistentstore/storetype/inmemory.md)
  An ephemeral store that reads from and writes to memory only.
- [static let sqlite: NSPersistentStore.StoreType](nspersistentstore/storetype/sqlite.md)
  A store that reads from and writes to a persistent SQLite database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/xml)*