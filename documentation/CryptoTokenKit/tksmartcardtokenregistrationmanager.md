# TKSmartCardTokenRegistrationManager

**Framework**: CryptoTokenKit  
**Kind**: class

Provides a centralized management system for registering and unregistering smartcards using their token IDs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager)*