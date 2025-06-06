# binary

**Framework**: Core Data  
**Kind**: property

A store that reads from and writes to a persistent binary file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static let binary: NSPersistentStore.StoreType
```

#### Discussion

A binary store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [`sqlite`](nspersistentstore/storetype/sqlite.md) store, which you can partially modify.

## See Also

- [static let inMemory: NSPersistentStore.StoreType](nspersistentstore/storetype/inmemory.md)
  An ephemeral store that reads from and writes to memory only.
- [static let sqlite: NSPersistentStore.StoreType](nspersistentstore/storetype/sqlite.md)
  A store that reads from and writes to a persistent SQLite database.
- [static let xml: NSPersistentStore.StoreType](nspersistentstore/storetype/xml.md)
  A store that reads from and writes to a persistent XML file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/binary)*