# configuration

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The current configuration for a token.

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
var configuration: TKToken.Configuration { get }
```

```objc
@property (readonly) TKTokenConfiguration * configuration;
```

## Discussion

Access keychain items exported by this token with the methods [`key(for:)`](./configuration-swift.class/key%28for%29.md) and [`certificate(for:)`](./configuration-swift.class/certificate%28for%29.md) provided by the configuration. You can access token-implementation-specific additional data using the [`configurationData`](./configuration-swift.class/configurationdata.md) property of the configuration.

## See Also

### Configuring the Token
- [TKToken.Configuration](./configuration-swift.class.md)
  A token’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.property)*