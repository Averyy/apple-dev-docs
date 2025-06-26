# changedPersistentIdentifier

**Framework**: SwiftData  
**Kind**: property  
**Required**: Yes

The changed persistent identifier of the delete operation.

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
var changedPersistentIdentifier: PersistentIdentifier { get }
```

## See Also

- [var changeIdentifier: Self.ChangeIdentifier](historydelete/changeidentifier-swift.property.md)
  The change identifier of the delete operation.
- [var tombstone: HistoryTombstone<Self.Model>](historydelete/tombstone.md)
  The value the framework uses to represent information about data the Swift Data previously deleted from a model.
- [var transactionIdentifier: Self.TransactionIdentifier](historydelete/transactionidentifier-swift.property.md)
  The delete operation’s transaction identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydelete/changedpersistentidentifier)*