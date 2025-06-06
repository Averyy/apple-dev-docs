# tokenDriver(_:terminateToken:)

**Framework**: CryptoTokenKit  
**Kind**: method

Tells the delegate to terminate the token you specify.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func tokenDriver(_ driver: TKTokenDriver, terminateToken token: TKToken)
```

## Parameters

- `driver`: The token driver.
- `token`: The token to be terminated.

## See Also

- [func tokenDriver(TKTokenDriver, tokenFor: TKToken.Configuration) throws -> TKToken](tktokendriverdelegate/tokendriver(_:tokenfor:).md)
  Creates a new token for the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/tokendriver(_:terminatetoken:))*