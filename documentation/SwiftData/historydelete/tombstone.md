# tombstone

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The value the framework uses to represent information about data the Swift Data previously deleted from a model.

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
var tombstone: HistoryTombstone<Self.Model> { get }
```

## See Also

### History deletion properites
- [var changeIdentifier: Self.ChangeIdentifier](./changeidentifier-swift.property.md)
  The change identifier of the delete operation.
- [var changedPersistentIdentifier: PersistentIdentifier](./changedpersistentidentifier.md)
  The changed persistent identifier of the delete operation.
- [var transactionIdentifier: Self.TransactionIdentifier](./transactionidentifier-swift.property.md)
  The delete operation’s transaction identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historydelete/tombstone)*