# CTSubscriberDelegate

**Framework**: Core Telephony  
**Kind**: protocol  
**Role**: Protocol

A protocol to handle changes to subscriber information.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 12.1+

## Declaration

```swift
protocol CTSubscriberDelegate
```

```objc
@protocol CTSubscriberDelegate
```

## Topics

### Handling Token Updates
- [func subscriberTokenRefreshed(CTSubscriber)](./ctsubscriberdelegate/subscribertokenrefreshed%28_%29.md)
  Tells the delegate the subscriber’s token refreshed.

## See Also

### Subscriber information
- [class CTSubscriber](./ctsubscriber.md)
  A cellular network subscriber.
- [class CTSubscriberInfo](./ctsubscriberinfo.md)
  An object that provides an array of cellular network subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriberdelegate)*