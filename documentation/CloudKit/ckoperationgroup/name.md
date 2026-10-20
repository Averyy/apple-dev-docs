# name

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The operation group’s name.

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
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

#### Discussion

The system sends the name of the operation group to CloudKit to provide aggregate reporting for [`CKOperationGroup`](../ckoperationgroup.md). The name must not include any personal data.

## See Also

### Configuring an Operation Group
- [var defaultConfiguration: CKOperation.Configuration!](./defaultconfiguration.md)
  The default configuration for operations in the group.
- [var expectedReceiveSize: CKOperationGroup.TransferSize](./expectedreceivesize.md)
  The estimated size of traffic to download from CloudKit.
- [var expectedSendSize: CKOperationGroup.TransferSize](./expectedsendsize.md)
  The estimated size of traffic to upload to CloudKit.
- [var operationGroupID: String](./operationgroupid.md)
  The operation group’s unique identifier.
- [var quantity: Int](./quantity.md)
  The number of operations in the operation group.
- [CKOperationGroup.TransferSize](./transfersize.md)
  Constants that represent possible data transfer sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/name)*