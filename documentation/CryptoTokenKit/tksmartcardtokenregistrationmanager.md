# TKSmartCardTokenRegistrationManager

**Framework**: CryptoTokenKit  
**Kind**: class

Provides a centralized management system for registering and unregistering smartcards using their token IDs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TKSmartCardTokenRegistrationManager
```

#### Overview

`Registered smartcard` keeps its itself accessible via Keychain and system will automatically invoke an NFC slot when a cryptographic operation is required and asks to provide the registered card.

## Topics

### Instance Properties
- [var registeredSmartCardTokens: [String]](tksmartcardtokenregistrationmanager/registeredsmartcardtokens.md)
  Returns the tokenIDs of all currently registered smart card tokens
### Instance Methods
- [func registerSmartCard(tokenID: String, promptMessage: String) throws](tksmartcardtokenregistrationmanager/registersmartcard(tokenid:promptmessage:).md)
  Registers a smartcard with a specific token ID.
- [func unregisterSmartCard(tokenID: String) throws](tksmartcardtokenregistrationmanager/unregistersmartcard(tokenid:).md)
  Unregisters a smartcard for the provided token ID.
### Type Properties
- [class var `default`: TKSmartCardTokenRegistrationManager](tksmartcardtokenregistrationmanager/default.md)
  Default instance of registration manager

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager)*