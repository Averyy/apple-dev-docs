# resultType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The type of result that Core Data returns from the request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resultType: NSBatchUpdateRequestResultType { get }
```

```objc
@property (readonly) NSBatchUpdateRequestResultType resultType;
```

## See Also

### Accessing Results
- [var result: Any?](./result.md)
  The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.
- [enum NSBatchUpdateRequestResultType](../nsbatchupdaterequestresulttype.md)
  Result types for a batch-update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdateresult/resulttype)*