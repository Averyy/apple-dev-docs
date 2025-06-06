# CTSubscriberInfo

**Framework**: Core Telephony  
**Kind**: class

An object that provides an array of cellular network subscribers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+

## Declaration

```swift
class CTSubscriberInfo
```

#### Overview

Use the [`CTSubscriber`](ctsubscriber.md) instances provided by this class to identify individual subscribers by their [`carrierToken`](ctsubscriber/carriertoken.md) or [`identifier`](ctsubscriber/identifier.md) properties.

## Topics

### Getting Subscriber Information
- [class func subscribers() -> [CTSubscriber]](ctsubscriberinfo/subscribers.md)
  Returns the cellular network subscribers.
- [class func subscriber() -> CTSubscriber](ctsubscriberinfo/subscriber.md)
  Returns the cellular network subscribers.

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

- [class CTSubscriber](ctsubscriber.md)
  A cellular network subscriber.
- [protocol CTSubscriberDelegate](ctsubscriberdelegate.md)
  A protocol to handle changes to subscriber information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo)*