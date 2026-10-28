# tokenDriver(_:tokenFor:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (TKToken *) tokenDriver:(TKTokenDriver *) driver tokenForConfiguration:(TKTokenConfiguration *) configuration error:(NSError **) error;
```

## Return Value

The created token.

## Discussion

The system invokes this method to request creation of a token instance, which the [`instanceID`](../tktoken/configuration-swift.class/instanceid.md) property of the configuration you specify identifies.

The created token has access to its current configuration using the [`configurationData`](../tktoken/configuration-swift.class/configurationdata.md) property, which can provide token-implementation-specific additional data. The token can access keychain items this token exports with the methods [`key(for:)`](../tktoken/configuration-swift.class/key%28for%29.md) and [`certificate(for:)`](../tktoken/configuration-swift.class/certificate%28for%29.md) that the configuration provides.

> **Note**:  Smart card token drivers must not implement this method.

## Parameters

- `driver`: The token driver.
- `configuration`: The configuration that identifies the token to create.

## See Also

### Creating and Removing Tokens
- [func tokenDriver(TKTokenDriver, terminateToken: TKToken)](./tokendriver%28_,terminatetoken%29.md)
  Tells the delegate to terminate the token you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/tokendriver(_:tokenfor:))*