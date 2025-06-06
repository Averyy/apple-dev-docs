# carrierToken

**Framework**: Core Telephony  
**Kind**: property

A data object containing authorization information about the subscriber.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

## Declaration

```swift
var carrierToken: Data? { get }
```

#### Discussion

May contain `nil` if no token is available.

The carrier API obtains this token from a carrier-provided server. The token authenticates your app to a server provided by the carrier, to prove that your app is running on a device owned by the subscriber.

## See Also

- [func refreshCarrierToken() -> Bool](ctsubscriber/refreshcarriertoken.md)
  Attempts to refresh the carrier token.
- [let CTSubscriberTokenRefreshed: String](ctsubscribertokenrefreshed.md)
  The name of the notification indicating that the carrier token is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber/carriertoken)*