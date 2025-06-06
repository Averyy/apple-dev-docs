# result

**Framework**: Core Data  
**Kind**: property

The value the request returns after it executes.

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
var result: Any? { get }
```

#### Discussion

Use [`resultType`](nsbatchdeleteresult/resulttype.md) to determine the kind of value this property contains, and then cast to the appropriate type as the following example shows:

```swift
// resultType is .resultTypeCount.
guard let count = batchDeleteResult.result as? Int else { return }
            
// resultType is .resultTypeObjectIDs.
guard let objectIDs = batchDeleteResult.result as? [NSManagedObjectID] 
    else { return }
            
// resultType is .resultTypeStatusOnly.
guard let status = batchDeleteResult.result as? Bool else { return }
```

## See Also

- [var resultType: NSBatchDeleteRequestResultType](nsbatchdeleteresult/resulttype.md)
  The data type of the request’s result value.
- [enum NSBatchDeleteRequestResultType](nsbatchdeleterequestresulttype.md)
  The types of result a batch delete request can provide when it executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/result)*