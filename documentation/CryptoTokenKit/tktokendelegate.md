# TKTokenDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol  
**Role**: Protocol

The interface that a token delegate implements to respond to session creation events.

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
protocol TKTokenDelegate : NSObjectProtocol
```

```objc
@protocol TKTokenDelegate <NSObject>
```

## Topics

### Delegate Methods
- [func createSession(TKToken) throws -> TKTokenSession](./tktokendelegate/createsession%28_%29.md)
  Tells the delegate to create a session for the specified token.
- [func token(TKToken, terminateSession: TKTokenSession)](./tktokendelegate/token%28_,terminatesession%29.md)
  Tells the delegate to terminate the specified token session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to Session Creation
- [var delegate: (any TKTokenDelegate)?](./tktoken/delegate.md)
  The token delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate)*