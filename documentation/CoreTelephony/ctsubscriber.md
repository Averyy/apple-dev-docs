# CTSubscriber

**Framework**: Core Telephony  
**Kind**: class

A cellular network subscriber.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

## Declaration

```swift
class CTSubscriber
```

## Topics

### Identifying the subscriber
- [var identifier: String](ctsubscriber/identifier.md)
  An implementation-defined identifier used to correlate this subscriber with information vended by other APIs.
### Working with a delegate
- [var delegate: (any CTSubscriberDelegate)?](ctsubscriber/delegate.md)
  A delegate that receives updates on the subscriber information.
### Managing the carrier token
- [var carrierToken: Data?](ctsubscriber/carriertoken.md)
  A data object containing authorization information about the subscriber.
- [func refreshCarrierToken() -> Bool](ctsubscriber/refreshcarriertoken.md)
  Attempts to refresh the carrier token.
- [let CTSubscriberTokenRefreshed: String](ctsubscribertokenrefreshed.md)
  The name of the notification indicating that the carrier token is available.
### Detecting a SIM
- [var isSIMInserted: Bool](ctsubscriber/issiminserted.md)
  A Boolean property that indicates whether a SIM is present.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol CTSubscriberDelegate](ctsubscriberdelegate.md)
  A protocol to handle changes to subscriber information.
- [class CTSubscriberInfo](ctsubscriberinfo.md)
  An object that provides an array of cellular network subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber)*