# TKToken

**Framework**: CryptoTokenKit  
**Kind**: class

A representation of a hardware-based cryptographic token.

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
class TKToken
```

#### Overview

> **Note**:  When working with smart card tokens, use or inherit from the [`TKSmartCardToken`](tksmartcardtoken.md) subclass instead.

## Topics

### Creating Tokens
- [init(tokenDriver: TKTokenDriver, instanceID: TKToken.InstanceID)](tktoken/init(tokendriver:instanceid:).md)
  Initializes a token with the driver you specify.
- [typealias InstanceID](tktoken/instanceid.md)
  A type that represents the instance identifier of a token.
### Responding to Session Creation
- [var delegate: (any TKTokenDelegate)?](tktoken/delegate.md)
  The token delegate.
- [protocol TKTokenDelegate](tktokendelegate.md)
  The interface that a token delegate implements to respond to session creation events.
### Accessing the Driver
- [var tokenDriver: TKTokenDriver](tktoken/tokendriver.md)
  The token driver.
### Accessing Keychain Items
- [var keychainContents: TKTokenKeychainContents?](tktoken/keychaincontents.md)
  The contents of the keychain for this token.
- [class TKTokenKeychainContents](tktokenkeychaincontents.md)
  A representation of the state of the keychain for a particular token.
- [class TKTokenKeychainItem](tktokenkeychainitem.md)
  An abstract base class for managing a token’s contents as keychain items.
- [class TKTokenKeychainCertificate](tktokenkeychaincertificate.md)
  A token’s certificate as stored in the keychain.
- [class TKTokenKeychainKey](tktokenkeychainkey.md)
  A token’s key as stored in the keychain.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
### Configuring the Token
- [var configuration: TKToken.Configuration](tktoken/configuration-swift.property.md)
  The current configuration for a token.
- [TKToken.Configuration](tktoken/configuration-swift.class.md)
  A token’s configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKSmartCardToken](tksmartcardtoken.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TKTokenWatcher](tktokenwatcher.md)
  An object that tracks the tokens available in the system.
- [class TKTokenDriver](tktokendriver.md)
  A base class for building token drivers.
- [class TKTokenSession](tktokensession.md)
  A token session that manages the authentication state of a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken)*