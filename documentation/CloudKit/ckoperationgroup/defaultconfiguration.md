# defaultConfiguration

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The default configuration for operations in the group.

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
@NSCopying
var defaultConfiguration: CKOperation.Configuration! { get set }
```

```objc
@property (copy, null_resettable) CKOperationConfiguration * defaultConfiguration;
```

#### Discussion

If an operation in the group has its own configuration, that configuration’s values override the default configuration’s values. For more information, see [`CKOperation.Configuration`](../ckoperation/configuration-swift.class.md).

## See Also

### Configuring an Operation Group
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
- [CKOperationGroup.TransferSize](./transfersize.md)
  Constants that represent possible data transfer sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/defaultconfiguration)*