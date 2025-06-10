# TKTokenDriver

**Framework**: CryptoTokenKit  
**Kind**: class

A base class for building token drivers.

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
class TKTokenDriver
```

#### Overview

When using the [`TKTokenDriver`](tktokendriver.md) class, implement the [`TKTokenDriverDelegate`](tktokendriverdelegate.md) protocol with the [`tokenDriver(_:tokenFor:)`](tktokendriverdelegate/tokendriver(_:tokenfor:).md) method, which the system invokes when it requests the creation of a token instance. After you create the token driver, it can examine [`keychainItems`](tktoken/configuration-swift.class/keychainitems.md) and [`configurationData`](tktoken/configuration-swift.class/configurationdata.md) to implement your desired functionality.

An implementation can also access its associated token configuration using the [`TKToken.Configuration`](tktoken/configuration-swift.class.md) property.

> **Note**:  When working with smart card tokens, use or inherit from the [`TKSmartCardTokenDriver`](tksmartcardtokendriver.md) subclass instead.

## Topics

### Responding to Token Creation
- [var delegate: (any TKTokenDriverDelegate)?](tktokendriver/delegate.md)
  The token driver delegate.
- [protocol TKTokenDriverDelegate](tktokendriverdelegate.md)
  The interface that a token driver delegate implements to respond to token creation events.
- [TKTokenDriver.ClassID](tktokendriver/classid.md)
  The type of the class identifier for the token driver.
- [TKTokenDriver.Configuration](tktokendriver/configuration.md)
  A configuration for one class of token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKSmartCardTokenDriver](tksmartcardtokendriver.md)
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
- [class TKToken](tktoken.md)
  A representation of a hardware-based cryptographic token.
- [class TKTokenSession](tktokensession.md)
  A token session that manages the authentication state of a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver)*