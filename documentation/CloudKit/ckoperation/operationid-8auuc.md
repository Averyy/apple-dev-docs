# operationID

**Framework**: CloudKit  
**Kind**: property

A unique identifier for a long-lived operation.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.2+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
var operationID: CKOperation.ID { get }
```

#### Discussion

Pass this property’s value to the [`fetchLongLivedOperationWithID:completionHandler:`](ckcontainer/fetchlonglivedoperationwithid:completionhandler:.md) method to fetch the corresponding long-lived operation. For more information, see [`Long-Lived Operations`](ckoperation#Long-Lived-Operations.md).

## See Also

- [CKOperation.ID](ckoperation/id.md)
  A type that represents the ID of an operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/operationid-8auuc)*