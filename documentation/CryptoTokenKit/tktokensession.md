# TKTokenSession

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A token session that manages the authentication state of a token.

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
class TKTokenSession
```

```objc
@interface TKTokenSession : NSObject
```

#### Overview

A token session communicates with its delegate to perform operations with its token that are bound to the authentication state.

A session is always instantiated by a [`TKToken`](./tktoken.md) instance through the token’s delegate when the framework detects access to the token from a new authentication session.

> ❗ **Important**:  Never share the authentication status of a token, such as the PIN entered to unlock a smart card, with other token sessions.

## Topics

### Creating Token Sessions
- [init(token: TKToken)](./tktokensession/init%28token%29.md)
  Initializes a token session with the specified token.
### Responding to Authentication Events
- [var delegate: (any TKTokenSessionDelegate)?](./tktokensession/delegate.md)
  The token session delegate.
- [protocol TKTokenSessionDelegate](./tktokensessiondelegate.md)
  The interface that a session instance delegate implements to respond to token session authentication events.
### Accessing the Token
- [var token: TKToken](./tktokensession/token.md)
  The token to which the session is bound.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [TKSmartCardTokenSession](./tksmartcardtokensession.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Tokens
- [class TKTokenWatcher](./tktokenwatcher.md)
  An object that tracks the tokens available in the system.
- [class TKTokenDriver](./tktokendriver.md)
  A base class for building token drivers.
- [class TKToken](./tktoken.md)
  A representation of a hardware-based cryptographic token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensession)*