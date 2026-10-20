# quantity

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The number of operations in the operation group.

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
var quantity: Int { get set }
```

```objc
@property (assign) NSUInteger quantity;
```

#### Discussion

This property shows the number of operations that you expect to be in this operation group. It’s the developer’s responsibility to set this value.

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
- [CKOperationGroup.TransferSize](./transfersize.md)
  Constants that represent possible data transfer sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup/quantity)*