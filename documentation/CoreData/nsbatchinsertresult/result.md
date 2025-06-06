# result

**Framework**: Core Data  
**Kind**: property

The result of a batch-insertion request.

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
var result: Any? { get }
```

#### Discussion

Cast the result to the type corresponding to [`resultType`](nsbatchinsertresult/resulttype.md) to inspect it. The following example shows how to inspect a result type of [`NSBatchInsertRequestResultType.statusOnly`](nsbatchinsertrequestresulttype/statusonly.md).

```swift
let success = batchInsertResult.result as? Bool
```

## See Also

- [var resultType: NSBatchInsertRequestResultType](nsbatchinsertresult/resulttype.md)
  The type of result that Core Data returns from this request.
- [enum NSBatchInsertRequestResultType](nsbatchinsertrequestresulttype.md)
  Result types for a batch-insertion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertresult/result)*