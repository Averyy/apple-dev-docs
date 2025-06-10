# CKOperationGroup

**Framework**: CloudKit  
**Kind**: class

An explicit association between two or more operations.

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
class CKOperationGroup
```

#### Overview

In certain situations, you might want to perform several CloudKit operations together. Grouping operations in CloudKit doesn’t ensure atomicity.

For example, when building a Calendar app, you group the following actions:

- Fetch records from CloudKit, which consists of numerous queries that fetch both new records and records with changes.
- Perform incremental fetches of records in response to a push notification.
- Update several records when the user saves a calendar event.

Associate operation groups with operations by setting their [`group`](ckoperation/group.md) property. Create a new operation group for each distinct user interaction.

## Topics

### Creating an Operation Group
- [init()](ckoperationgroup/init.md)
  Creates an operation group.
- [init(coder: NSCoder)](ckoperationgroup/init(coder:).md)
  Creates an operation group from a serialized instance.
### Configuring an Operation Group
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
- [CKOperationGroup.TransferSize](ckoperationgroup/transfersize.md)
  Constants that represent possible data transfer sizes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKContainer](ckcontainer.md)
  A conduit to your app’s databases.
- [class CKDatabase](ckdatabase.md)
  An object that represents a collection of record zones and subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperationgroup)*