# CXCallController

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

A programmatic interface for interacting with and observing calls.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXCallController
```

```objc
@interface CXCallController : NSObject
```

#### Overview

A [`CXCallController`](./cxcallcontroller.md) object interacts with calls by performing actions, which are represented by instances of [`CXCallAction`](./cxcallaction.md) subclasses. You can request that one or more actions be performed in a single [`CXTransaction`](./cxtransaction.md) object using the [`request(_:completion:)`](./cxcallcontroller/request%28_,completion%29.md) method. A transaction may be rejected by the system for one of the reasons listed in the [`CXErrorCodeRequestTransactionError.Code`](./cxerrorcoderequesttransactionerror-swift.struct/code.md) enumeration.

Each [`CXCallController`](./cxcallcontroller.md) object manages a [`CXCallObserver`](./cxcallobserver.md) object, which can be accessed using the [`callObserver`](./cxcallcontroller/callobserver.md) property. You can provide an object conforming to the [`CXCallObserverDelegate`](./cxcallobserverdelegate.md) protocol to the call observer in order to be notified of any changes to active calls.

## Topics

### Creating New Call Controllers
- [convenience init()](./cxcallcontroller/init%28%29.md)
  Initializes a new call controller with a private, serial queue, which is used for calling completion blocks.
- [init(queue: dispatch_queue_t)](./cxcallcontroller/init%28queue%29.md)
  Initializes a new call controller with a specified queue, which is used for calling completion blocks.
### Accessing the Call Observer
- [var callObserver: CXCallObserver](./cxcallcontroller/callobserver.md)
  Returns an observer for active calls.
### Requesting Transactions
- [func request(CXTransaction, completion: ((any Error)?) -> Void)](./cxcallcontroller/request%28_,completion%29.md)
  Requests that the actions in the specified transaction be asynchronously performed by the telephony provider.
- [func requestTransaction(with: CXAction, completion: ((any Error)?) -> Void)](./cxcallcontroller/requesttransaction%28with,completion%29-ffme.md)
  Requests that the transaction that contains the specified action be asynchronously performed by the telephony provider.
- [func requestTransaction(with: [CXAction], completion: ((any Error)?) -> Void)](./cxcallcontroller/requesttransaction%28with,completion%29-4o1m4.md)
  Requests that the transaction that contains the specified actions be asynchronously performed by the telephony provider.
### Errors
- [struct CXErrorCodeRequestTransactionError](./cxerrorcoderequesttransactionerror-swift.struct.md)
- [CXErrorCodeRequestTransactionError.Code](./cxerrorcoderequesttransactionerror-swift.struct/code.md)
  Error codes for the CallKit error domain.
- [let CXErrorDomainRequestTransaction: String](./cxerrordomainrequesttransaction.md)
  Domain for errors when requesting a transaction from a call controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Outgoing calls
- [Sending End-to-End Encrypted VoIP Calls](./sending-end-to-end-encrypted-voip-calls.md)
  Initiate VoIP calls when your server can’t determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- [class CXTransaction](./cxtransaction.md)
  An object that contains zero or more action objects for a call controller to perform.
- [class CXStartCallAction](./cxstartcallaction.md)
  An encapsulation of the act of initiating an outgoing call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallcontroller)*