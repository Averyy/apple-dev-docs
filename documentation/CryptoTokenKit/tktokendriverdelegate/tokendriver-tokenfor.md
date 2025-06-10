# tokenDriver(_:tokenFor:)

**Framework**: CryptoTokenKit  
**Kind**: method

Creates a new token for the configuration you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func tokenDriver(_ driver: TKTokenDriver, tokenFor configuration: TKToken.Configuration) throws -> TKToken
```

#### Return Value

The created token.

#### Discussion

The system invokes this method to request creation of a token instance, which the [`instanceID`](tktoken/configuration-swift.class/instanceid.md) property of the configuration you specify identifies.

The created token has access to its current configuration using the [`configurationData`](tktoken/configuration-swift.class/configurationdata.md) property, which can provide token-implementation-specific additional data. The token can access keychain items this token exports with the methods [`key(for:)`](tktoken/configuration-swift.class/key(for:).md) and [`certificate(for:)`](tktoken/configuration-swift.class/certificate(for:).md) that the configuration provides.

> **Note**:  Smart card token drivers must not implement this method.

## Parameters

- `driver`: The token driver.
- `configuration`: The configuration that identifies the token to create.

## See Also

- [func tokenDriver(TKTokenDriver, terminateToken: TKToken)](tktokendriverdelegate/tokendriver(_:terminatetoken:).md)
  Tells the delegate to terminate the token you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/tokendriver(_:tokenfor:))*