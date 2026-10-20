# tokenDriver(_:terminateToken:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) tokenDriver:(TKTokenDriver *) driver terminateToken:(TKToken *) token;
```

## Parameters

- `driver`: The token driver.
- `token`: The token to be terminated.

## See Also

### Creating and Removing Tokens
- [func tokenDriver(TKTokenDriver, tokenFor: TKToken.Configuration) throws -> TKToken](./tokendriver%28_,tokenfor%29.md)
  Creates a new token for the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/tokendriver(_:terminatetoken:))*