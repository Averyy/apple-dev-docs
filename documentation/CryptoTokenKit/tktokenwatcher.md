# TKTokenWatcher

**Framework**: CryptoTokenKit  
**Kind**: class

An object that tracks the tokens available in the system.

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
class TKTokenWatcher
```

## Mentions

- [Using Cryptographic Assets Stored on a Smart Card](using-cryptographic-assets-stored-on-a-smart-card.md)

#### Overview

Create a token watcher and register an insertion handler to be notified when tokens are added to the system. You can also add removal handlers for specific tokens to be notified when those tokens are removed from the system.

## Topics

### Creating Token Watchers
- [init()](tktokenwatcher/init.md)
  Initializes a token watcher.
- [init(insertionHandler: (String) -> Void)](tktokenwatcher/init(insertionhandler:).md)
  Initializes a token watcher with the specified insertion handler.
### Accessing Token Identifiers
- [var tokenIDs: [String]](tktokenwatcher/tokenids.md)
  The token IDs currently available in the system.
### Configuring Handlers
- [func addRemovalHandler((String) -> Void, forTokenID: String)](tktokenwatcher/addremovalhandler(_:fortokenid:).md)
  Adds a removal handler for the specified token ID.
- [func setInsertionHandler((String) -> Void)](tktokenwatcher/setinsertionhandler(_:).md)
  Sets an insertion handler closure to be called when a new token is inserted into the system.
### Classes
- [TKTokenWatcher.TokenInfo](tktokenwatcher/tokeninfo.md)
### Instance Methods
- [func tokenInfo(forTokenID: String) -> TKTokenWatcher.TokenInfo?](tktokenwatcher/tokeninfo(fortokenid:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TKTokenDriver](tktokendriver.md)
  A base class for building token drivers.
- [class TKToken](tktoken.md)
  A representation of a hardware-based cryptographic token.
- [class TKTokenSession](tktokensession.md)
  A token session that manages the authentication state of a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher)*