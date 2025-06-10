# CTSubscriberTokenRefreshed

**Framework**: Core Telephony  
**Kind**: var

The name of the notification indicating that the carrier token is available.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let CTSubscriberTokenRefreshed: String
```

#### Discussion

The notification’s [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) property is the [`CTSubscriber`](ctsubscriber.md) instance whose subscriber token refreshed.

## See Also

- [var carrierToken: Data?](ctsubscriber/carriertoken.md)
  A data object containing authorization information about the subscriber.
- [func refreshCarrierToken() -> Bool](ctsubscriber/refreshcarriertoken.md)
  Attempts to refresh the carrier token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscribertokenrefreshed)*