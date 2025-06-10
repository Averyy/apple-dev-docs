# NSBatchDeleteRequestResultType

**Framework**: Core Data  
**Kind**: enum

The types of result a batch delete request can provide when it executes.

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
enum NSBatchDeleteRequestResultType
```

## Topics

### Result Types
- [NSBatchDeleteRequestResultType.resultTypeCount](nsbatchdeleterequestresulttype/resulttypecount.md)
  Returns the number of managed objects the request deletes.
- [NSBatchDeleteRequestResultType.resultTypeObjectIDs](nsbatchdeleterequestresulttype/resulttypeobjectids.md)
  Returns an array of the deleted managed objects’ identifiers.
- [NSBatchDeleteRequestResultType.resultTypeStatusOnly](nsbatchdeleterequestresulttype/resulttypestatusonly.md)
  Returns a Boolean value that indicates if the request succeeds.
### Initializers
- [init?(rawValue: UInt)](nsbatchdeleterequestresulttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var resultType: NSBatchDeleteRequestResultType](nsbatchdeleterequest/resulttype.md)
  The type of result the request provides when it executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)*