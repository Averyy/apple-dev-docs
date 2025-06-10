# NSPersistentHistoryResultType

**Framework**: Core Data  
**Kind**: enum

The types of results from a persistent history change request.

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
enum NSPersistentHistoryResultType
```

## Topics

### Result Types
- [NSPersistentHistoryResultType.statusOnly](nspersistenthistoryresulttype/statusonly.md)
  The status of the persistent history change request.
- [NSPersistentHistoryResultType.count](nspersistenthistoryresulttype/count.md)
  The number of persistent history changes since the requested date, token, or transaction.
- [NSPersistentHistoryResultType.objectIDs](nspersistenthistoryresulttype/objectids.md)
  The identifiers of managed objects changed since the requested date, token, or transaction.
- [NSPersistentHistoryResultType.transactionsAndChanges](nspersistenthistoryresulttype/transactionsandchanges.md)
  The persistent history transactions and changes since the requested date, token, or transaction.
- [NSPersistentHistoryResultType.transactionsOnly](nspersistenthistoryresulttype/transactionsonly.md)
  The persistent history transactions since the requested date, token, or transaction.
- [NSPersistentHistoryResultType.changesOnly](nspersistenthistoryresulttype/changesonly.md)
  The persistent history changes since the requested date, token, or transaction.
### Initializers
- [init?(rawValue: Int)](nspersistenthistoryresulttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var result: Any?](nspersistenthistoryresult/result.md)
  The result of the history request determined by the persistent history result type.
- [var resultType: NSPersistentHistoryResultType](nspersistenthistoryresult/resulttype.md)
  The type of result that the persistent history change request returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistoryresulttype)*