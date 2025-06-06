# expectedReceiveSize

**Framework**: CloudKit  
**Kind**: property

The estimated size of traffic to download from CloudKit.

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
var expectedReceiveSize: CKOperationGroup.TransferSize { get set }
```

#### Discussion

This property informs the system about the amount of data your app can transfer. An order-of-magnitude estimate is better than no estimate, and accuracy helps performance. The system checks this value when it schedules discretionary network requests.

## See Also

- [var defaultConfiguration: CKOperation.Configuration!](ckoperationgroup/defaultconfiguration.md)
  The default configuration for operations in the group.
- [var expectedSendSize: CKOperationGroup.TransferSize](ckoperationgroup/expectedsendsize.md)
  The estimated size of traffic to upload to CloudKit.
- [var name: String?](ckoperationgroup/name.md)
  The operation group’s name.
- [var operationGroupID: String](ckoperationgroup/operationgroupid.md)
  The operation group’s unique identifier.
- [var quantity: Int](ckoperationgroup/quantity.md)
  The number of operations in the operation group.
- [CKOperationGroup.TransferSize](ckoperationgroup/transfersize.md)
  Constants that represent possible data transfer sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/expectedreceivesize)*