# NSPersistentHistoryResult

**Framework**: Core Data  
**Kind**: class

The result of a request to fetch persistent history.

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
class NSPersistentHistoryResult
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

## Topics

### Inspecting History Results
- [var result: Any?](nspersistenthistoryresult/result.md)
  The result of the history request determined by the persistent history result type.
- [var resultType: NSPersistentHistoryResultType](nspersistenthistoryresult/resulttype.md)
  The type of result that the persistent history change request returns.
- [enum NSPersistentHistoryResultType](nspersistenthistoryresulttype.md)
  The types of results from a persistent history change request.

## Relationships

### Inherits From
- [NSPersistentStoreResult](nspersistentstoreresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentHistoryChangeRequest](nspersistenthistorychangerequest.md)
  A request to fetch or purge persistent history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistoryresult)*