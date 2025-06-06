# NSBatchUpdateResult

**Framework**: Core Data  
**Kind**: class

The result returned when executing a batch update request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSBatchUpdateResult
```

## Topics

### Accessing Results
- [var result: Any?](nsbatchupdateresult/result.md)
  The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.
- [var resultType: NSBatchUpdateRequestResultType](nsbatchupdateresult/resulttype.md)
  The type of result that Core Data returns from the request.
- [enum NSBatchUpdateRequestResultType](nsbatchupdaterequestresulttype.md)
  Result types for a batch-update request.

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

- [class NSBatchUpdateRequest](nsbatchupdaterequest.md)
  A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdateresult)*