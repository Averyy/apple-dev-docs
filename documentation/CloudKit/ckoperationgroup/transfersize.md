# CKOperationGroup.TransferSize

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CKOperationGroupTransferSize : NSInteger;
```

## Topics

### Transfer Sizes
- [CKOperationGroup.TransferSize.kilobytes](./transfersize/kilobytes.md)
  A transfer size that represents 1 or more kilobytes.
- [CKOperationGroup.TransferSize.megabytes](./transfersize/megabytes.md)
  A transfer size that represents 1 or more megabytes.
- [CKOperationGroup.TransferSize.gigabytes](./transfersize/gigabytes.md)
  A transfer size that represents 1 or more gigabytes.
- [CKOperationGroup.TransferSize.tensOfMegabytes](./transfersize/tensofmegabytes.md)
  A transfer size that represents tens of megabytes.
- [CKOperationGroup.TransferSize.tensOfGigabytes](./transfersize/tensofgigabytes.md)
  A transfer size that represents tens of gigabytes.
- [CKOperationGroup.TransferSize.hundredsOfMegabytes](./transfersize/hundredsofmegabytes.md)
  A transfer size that represents hundreds of megabytes.
- [CKOperationGroup.TransferSize.hundredsOfGigabytes](./transfersize/hundredsofgigabytes.md)
  A transfer size that represents hundreds of gigabytes.
- [CKOperationGroup.TransferSize.unknown](./transfersize/unknown.md)
  An unknown transfer size.
### Initializers
- [init?(rawValue: Int)](./transfersize/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring an Operation Group
- [var defaultConfiguration: CKOperation.Configuration!](./defaultconfiguration.md)
  The default configuration for operations in the group.
- [var expectedReceiveSize: CKOperationGroup.TransferSize](./expectedreceivesize.md)
  The estimated size of traffic to download from CloudKit.
- [var expectedSendSize: CKOperationGroup.TransferSize](./expectedsendsize.md)
  The estimated size of traffic to upload to CloudKit.
- [var name: String?](./name.md)
  The operation group’s name.
- [var operationGroupID: String](./operationgroupid.md)
  The operation group’s unique identifier.
- [var quantity: Int](./quantity.md)
  The number of operations in the operation group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/transfersize)*