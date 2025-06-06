# CKOperationGroup.TransferSize

**Framework**: CloudKit  
**Kind**: enum

Constants that represent possible data transfer sizes.

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
enum TransferSize
```

## Topics

### Transfer Sizes
- [CKOperationGroup.TransferSize.kilobytes](ckoperationgroup/transfersize/kilobytes.md)
  A transfer size that represents 1 or more kilobytes.
- [CKOperationGroup.TransferSize.megabytes](ckoperationgroup/transfersize/megabytes.md)
  A transfer size that represents 1 or more megabytes.
- [CKOperationGroup.TransferSize.gigabytes](ckoperationgroup/transfersize/gigabytes.md)
  A transfer size that represents 1 or more gigabytes.
- [CKOperationGroup.TransferSize.tensOfMegabytes](ckoperationgroup/transfersize/tensofmegabytes.md)
  A transfer size that represents tens of megabytes.
- [CKOperationGroup.TransferSize.tensOfGigabytes](ckoperationgroup/transfersize/tensofgigabytes.md)
  A transfer size that represents tens of gigabytes.
- [CKOperationGroup.TransferSize.hundredsOfMegabytes](ckoperationgroup/transfersize/hundredsofmegabytes.md)
  A transfer size that represents hundreds of megabytes.
- [CKOperationGroup.TransferSize.hundredsOfGigabytes](ckoperationgroup/transfersize/hundredsofgigabytes.md)
  A transfer size that represents hundreds of gigabytes.
- [CKOperationGroup.TransferSize.unknown](ckoperationgroup/transfersize/unknown.md)
  An unknown transfer size.
### Initializers
- [init?(rawValue: Int)](ckoperationgroup/transfersize/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var defaultConfiguration: CKOperation.Configuration!](ckoperationgroup/defaultconfiguration.md)
  The default configuration for operations in the group.
- [var expectedReceiveSize: CKOperationGroup.TransferSize](ckoperationgroup/expectedreceivesize.md)
  The estimated size of traffic to download from CloudKit.
- [var expectedSendSize: CKOperationGroup.TransferSize](ckoperationgroup/expectedsendsize.md)
  The estimated size of traffic to upload to CloudKit.
- [var name: String?](ckoperationgroup/name.md)
  The operation group’s name.
- [var operationGroupID: String](ckoperationgroup/operationgroupid.md)
  The operation group’s unique identifier.
- [var quantity: Int](ckoperationgroup/quantity.md)
  The number of operations in the operation group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/transfersize)*