# CXTransaction

**Framework**: CallKit  
**Kind**: class

An object that contains zero or more action objects for a call controller to perform.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXTransaction
```

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

## Topics

### Creating New Transactions
- [convenience init(action: CXAction)](cxtransaction/init(action:).md)
  Initializes a new transaction with the specified action.
- [init(actions: [CXAction])](cxtransaction/init(actions:).md)
  Initializes a new transaction with the specified actions.
### Accessing Transaction Attributes
- [var uuid: UUID](cxtransaction/uuid.md)
  The unique identifier of the transaction.
- [var isComplete: Bool](cxtransaction/iscomplete.md)
  A Boolean value that indicates whether the transaction has been completed.
- [var actions: [CXAction]](cxtransaction/actions.md)
  The actions added to a transaction.
### Adding Actions
- [func addAction(CXAction)](cxtransaction/addaction(_:).md)
  Adds the specified action to the transaction.

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

## See Also

- [Sending End-to-End Encrypted VoIP Calls](sending-end-to-end-encrypted-voip-calls.md)
  Initiate VoIP calls when your server can’t determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- [class CXCallController](cxcallcontroller.md)
  A programmatic interface for interacting with and observing calls.
- [class CXStartCallAction](cxstartcallaction.md)
  An encapsulation of the act of initiating an outgoing call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction)*