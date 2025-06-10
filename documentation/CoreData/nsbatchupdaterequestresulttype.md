# NSBatchUpdateRequestResultType

**Framework**: Core Data  
**Kind**: enum

Result types for a batch-update request.

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
enum NSBatchUpdateRequestResultType
```

## Topics

### Request Types
- [NSBatchUpdateRequestResultType.statusOnlyResultType](nsbatchupdaterequestresulttype/statusonlyresulttype.md)
  A value that indicates the return type is a Boolean value representing whether the batch-update request succeeds.
- [NSBatchUpdateRequestResultType.updatedObjectIDsResultType](nsbatchupdaterequestresulttype/updatedobjectidsresulttype.md)
  A value that indicates the return type is an array of object IDs that corresponds to the updated rows.
- [NSBatchUpdateRequestResultType.updatedObjectsCountResultType](nsbatchupdaterequestresulttype/updatedobjectscountresulttype.md)
  A value that indicates the return type is the number of updated rows.
### Initializers
- [init?(rawValue: UInt)](nsbatchupdaterequestresulttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var result: Any?](nsbatchupdateresult/result.md)
  The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.
- [var resultType: NSBatchUpdateRequestResultType](nsbatchupdateresult/resulttype.md)
  The type of result that Core Data returns from the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype)*