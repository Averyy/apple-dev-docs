# CTSubscriberInfo

**Framework**: Core Telephony  
**Kind**: class  
**Role**: Class

An object that provides an array of cellular network subscribers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+

## Declaration

```swift
class CTSubscriberInfo
```

```objc
@interface CTSubscriberInfo : NSObject
```

#### Overview

Use the [`CTSubscriber`](./ctsubscriber.md) instances provided by this class to identify individual subscribers by their [`carrierToken`](./ctsubscriber/carriertoken.md) or [`identifier`](./ctsubscriber/identifier.md) properties.

## Topics

### Getting Subscriber Information
- [class func subscribers() -> [CTSubscriber]](./ctsubscriberinfo/subscribers%28%29.md)
  Returns the cellular network subscribers.
- [class func subscriber() -> CTSubscriber](./ctsubscriberinfo/subscriber%28%29.md)
  Returns the cellular network subscribers.

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

### Subscriber information
- [class CTSubscriber](./ctsubscriber.md)
  A cellular network subscriber.
- [protocol CTSubscriberDelegate](./ctsubscriberdelegate.md)
  A protocol to handle changes to subscriber information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo)*