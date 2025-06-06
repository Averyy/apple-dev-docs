# NSBatchInsertResult

**Framework**: Core Data  
**Kind**: class

The result that Core Data returns when executing a batch-insertion request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NSBatchInsertResult
```

## Topics

### Accessing Results
- [var result: Any?](nsbatchinsertresult/result.md)
  The result of a batch-insertion request.
- [var resultType: NSBatchInsertRequestResultType](nsbatchinsertresult/resulttype.md)
  The type of result that Core Data returns from this request.
- [enum NSBatchInsertRequestResultType](nsbatchinsertrequestresulttype.md)
  Result types for a batch-insertion request.

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

- [class NSBatchInsertRequest](nsbatchinsertrequest.md)
  A request to insert a batch of data in a persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertresult)*