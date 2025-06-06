# operationGroupID

**Framework**: CloudKit  
**Kind**: property

The operation group’s unique identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var operationGroupID: String { get }
```

#### Discussion

The framework generates this value and it’s unique to this operation group. The system sends this identifier to CloudKit, which can use it to identify server-side logs for [`CKOperationGroup`](ckoperationgroup.md).

## See Also

- [var defaultConfiguration: CKOperation.Configuration!](ckoperationgroup/defaultconfiguration.md)
  The default configuration for operations in the group.
- [var expectedReceiveSize: CKOperationGroup.TransferSize](ckoperationgroup/expectedreceivesize.md)
  The estimated size of traffic to download from CloudKit.
- [var expectedSendSize: CKOperationGroup.TransferSize](ckoperationgroup/expectedsendsize.md)
  The estimated size of traffic to upload to CloudKit.
- [var name: String?](ckoperationgroup/name.md)
  The operation group’s name.
- [var quantity: Int](ckoperationgroup/quantity.md)
  The number of operations in the operation group.
- [CKOperationGroup.TransferSize](ckoperationgroup/transfersize.md)
  Constants that represent possible data transfer sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/operationgroupid)*