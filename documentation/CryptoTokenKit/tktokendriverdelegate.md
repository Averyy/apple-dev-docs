# TKTokenDriverDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol  
**Role**: Protocol

The interface that a token driver delegate implements to respond to token creation events.

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
protocol TKTokenDriverDelegate : NSObjectProtocol
```

```objc
@protocol TKTokenDriverDelegate <NSObject>
```

## Topics

### Creating and Removing Tokens
- [func tokenDriver(TKTokenDriver, terminateToken: TKToken)](./tktokendriverdelegate/tokendriver%28_,terminatetoken%29.md)
  Tells the delegate to terminate the token you specify.
- [func tokenDriver(TKTokenDriver, tokenFor: TKToken.Configuration) throws -> TKToken](./tktokendriverdelegate/tokendriver%28_,tokenfor%29.md)
  Creates a new token for the configuration you specify.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [TKSmartCardTokenDriverDelegate](./tksmartcardtokendriverdelegate.md)

## See Also

### Responding to Token Creation
- [var delegate: (any TKTokenDriverDelegate)?](./tktokendriver/delegate.md)
  The token driver delegate.
- [TKTokenDriver.ClassID](./tktokendriver/classid.md)
  The type of the class identifier for the token driver.
- [TKTokenDriver.Configuration](./tktokendriver/configuration.md)
  A configuration for one class of token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate)*