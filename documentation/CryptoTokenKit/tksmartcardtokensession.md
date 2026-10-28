# TKSmartCardTokenSession

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A token session that is based on a smart card token.

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
class TKSmartCardTokenSession
```

```objc
@interface TKSmartCardTokenSession : TKTokenSession
```

## Mentions

- [Authenticating Users with a Cryptographic Token](./authenticating-users-with-a-cryptographic-token.md)

## Overview

You can use the [`smartCard`](./tksmartcardtokensession/smartcard.md) property to access and send APDUs to the underlying smart card.

## Topics

### Accessing the Smart Card
- [var smartCard: TKSmartCard](./tksmartcardtokensession/smartcard.md)
  The smart card for the active exclusive session and selected application.
### Instance Methods
- [func getSmartCard() throws -> TKSmartCard](./tksmartcardtokensession/getsmartcard%28%29.md)

## Relationships

### Inherits From
- [TKTokenSession](./tktokensession.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Smart Card App Extensions
- [Authenticating Users with a Cryptographic Token](./authenticating-users-with-a-cryptographic-token.md)
  Grant access to user accounts and the keychain by creating a smart card app extension.
- [Configuring Smart Card Authentication](./configuring-smart-card-authentication.md)
  Set preferences for smart card authentication operations, including those on managed devices.
- [class TKSmartCardTokenDriver](./tksmartcardtokendriver.md)
  The driver that acts as an entry point for smart card app extensions.
- [class TKSmartCardToken](./tksmartcardtoken.md)
  A representation of a smart card based cryptographic token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession)*