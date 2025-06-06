# changes

**Framework**: Core Data  
**Kind**: property

The array of persistent history changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var changes: [NSPersistentHistoryChange]? { get }
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

## See Also

- [var author: String?](nspersistenthistorytransaction/author.md)
  A granular description of the context that made the persistent history change, if available.
- [var bundleID: String](nspersistenthistorytransaction/bundleid.md)
  The originating bundle’s identifier.
- [var contextName: String?](nspersistenthistorytransaction/contextname.md)
  The originating context’s name.
- [var processID: String](nspersistenthistorytransaction/processid.md)
  The originating process’s identifier.
- [var storeID: String](nspersistenthistorytransaction/storeid.md)
  The originating store’s identifier.
- [var timestamp: Date](nspersistenthistorytransaction/timestamp.md)
  The date of the persistent history change.
- [var token: NSPersistentHistoryToken](nspersistenthistorytransaction/token.md)
  The token that represents this transaction in the persistent history.
- [var transactionNumber: Int64](nspersistenthistorytransaction/transactionnumber.md)
  The transaction’s numeric identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/changes)*