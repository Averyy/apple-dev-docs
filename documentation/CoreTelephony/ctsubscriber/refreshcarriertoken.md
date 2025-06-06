# refreshCarrierToken()

**Framework**: Coretelephony  
**Kind**: method

Attempts to refresh the carrier token.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+

## Declaration

```swift
func refreshCarrierToken() -> Bool
```

#### Return Value

`true` if the system performs a token refresh in response to this call; otherwise, `false`.

#### Discussion

Call this method to update the [`carrierToken`](ctsubscriber/carriertoken.md) when the token exists but the server rejects it.

> **Note**:  Retrieve and attempt to use `carrierToken` first. Only call this method when you know the token is invalid.

Inspect the return value to determine whether this call results in an actual refresh. If the return value is `true`, the system attempts the refresh and calls the delegate method [`subscriberTokenRefreshed(_:)`](ctsubscriberdelegate/subscribertokenrefreshed(_:).md). A return value of `false` indicates an invalid argument (such as bad carrier descriptors or service descriptor) or that the subscriber doesn’t support the authentication action.

## See Also

- [var carrierToken: Data?](ctsubscriber/carriertoken.md)
  A data object containing authorization information about the subscriber.
- [let CTSubscriberTokenRefreshed: String](ctsubscribertokenrefreshed.md)
  The name of the notification indicating that the carrier token is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber/refreshcarriertoken())*