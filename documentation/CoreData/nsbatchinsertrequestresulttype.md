# NSBatchInsertRequestResultType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

Result types for a batch-insertion request.

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
enum NSBatchInsertRequestResultType
```

```c
enum NSBatchInsertRequestResultType : NSUInteger;
```

## Topics

### Request Types
- [NSBatchInsertRequestResultType.statusOnly](./nsbatchinsertrequestresulttype/statusonly.md)
  A value that indicates that the return type is a Boolean value representing whether the batch-insertion request succeeded.
- [NSBatchInsertRequestResultType.objectIDs](./nsbatchinsertrequestresulttype/objectids.md)
  A value that indicates the return type is an array of object IDs that corresponds to the inserted rows.
- [NSBatchInsertRequestResultType.count](./nsbatchinsertrequestresulttype/count.md)
  A value that indicates that the return type is the number of inserted rows.
### Initializers
- [init?(rawValue: UInt)](./nsbatchinsertrequestresulttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Results
- [var result: Any?](./nsbatchinsertresult/result.md)
  The result of a batch-insertion request.
- [var resultType: NSBatchInsertRequestResultType](./nsbatchinsertresult/resulttype.md)
  The type of result that Core Data returns from this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequestresulttype)*