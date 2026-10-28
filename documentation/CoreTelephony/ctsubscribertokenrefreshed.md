# CTSubscriberTokenRefreshed

**Framework**: Core Telephony  
**Kind**: var  
**Role**: Global Variable

The name of the notification indicating that the carrier token is available.

**Availability**:
- iOS 7.0+ - Deprecated in 12.1
- iPadOS 7.0+ - Deprecated in 12.1
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CTSubscriberDelegate`](./ctsubscriberdelegate.md) method [`subscriberTokenRefreshed(_:)`](./ctsubscriberdelegate/subscribertokenrefreshed%28_%29.md) instead.

## Declaration

```swift
let CTSubscriberTokenRefreshed: String
```

```c
extern NSString * const CTSubscriberTokenRefreshed;
```

## Discussion

The notification’s [`object`](../Foundation/nsnotification/object.md) property is the [`CTSubscriber`](./ctsubscriber.md) instance whose subscriber token refreshed.

## See Also

### Managing the carrier token
- [var carrierToken: Data?](./ctsubscriber/carriertoken.md)
  A data object containing authorization information about the subscriber.
- [func refreshCarrierToken() -> Bool](./ctsubscriber/refreshcarriertoken%28%29.md)
  Attempts to refresh the carrier token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscribertokenrefreshed)*