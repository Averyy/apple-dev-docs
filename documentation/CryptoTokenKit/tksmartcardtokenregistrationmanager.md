# TKSmartCardTokenRegistrationManager

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKSmartCardTokenRegistrationManager : NSObject
```

#### Overview

`Registered smartcard` keeps its itself accessible via Keychain and system will automatically invoke an NFC slot when a cryptographic operation is required and asks to provide the registered card.

## Topics

### Instance Properties
- [var registeredSmartCardTokens: [String]](./tksmartcardtokenregistrationmanager/registeredsmartcardtokens.md)
  Returns the tokenIDs of all currently registered smart card tokens
### Instance Methods
- [func registerSmartCard(tokenID: String, promptMessage: String) throws](./tksmartcardtokenregistrationmanager/registersmartcard%28tokenid,promptmessage%29.md)
  Registers a smartcard with a specific token ID.
- [func unregisterSmartCard(tokenID: String) throws](./tksmartcardtokenregistrationmanager/unregistersmartcard%28tokenid%29.md)
  Unregisters a smartcard for the provided token ID.
### Type Properties
- [class var `default`: TKSmartCardTokenRegistrationManager](./tksmartcardtokenregistrationmanager/default.md)
  Default instance of registration manager

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager)*