# resultType

**Framework**: Core Data  
**Kind**: property

The type of result the request provides when it executes.

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
var resultType: NSBatchDeleteRequestResultType { get set }
```

#### Discussion

Set this property before you execute the request if you require a result type other than the default of [`NSBatchDeleteRequestResultType.resultTypeStatusOnly`](nsbatchdeleterequestresulttype/resulttypestatusonly.md).

## See Also

- [enum NSBatchDeleteRequestResultType](nsbatchdeleterequestresulttype.md)
  The types of result a batch delete request can provide when it executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/resulttype)*