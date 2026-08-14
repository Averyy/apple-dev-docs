# NSBatchDeleteResult

**Framework**: Core Data  
**Kind**: class

An object that describes the result of a batch delete request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSBatchDeleteResult
```

## Topics

### Accessing the Result
- [var result: Any?](nsbatchdeleteresult/result.md)
  The value the request returns after it executes.
- [var resultType: NSBatchDeleteRequestResultType](nsbatchdeleteresult/resulttype.md)
  The data type of the request’s result value.
- [enum NSBatchDeleteRequestResultType](nsbatchdeleterequestresulttype.md)
  The types of result a batch delete request can provide when it executes.

## Relationships

### Inherits From
- [NSPersistentStoreResult](nspersistentstoreresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSBatchDeleteRequest](nsbatchdeleterequest.md)
  A request that deletes objects in the SQLite persistent store without loading them into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)*