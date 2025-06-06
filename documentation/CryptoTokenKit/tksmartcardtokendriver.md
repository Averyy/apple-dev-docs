# TKSmartCardTokenDriver

**Framework**: CryptoTokenKit  
**Kind**: class

The driver that acts as an entry point for smart card app extensions.

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
class TKSmartCardTokenDriver
```

## Mentions

- [Authenticating Users with a Cryptographic Token](authenticating-users-with-a-cryptographic-token.md)

## Topics

### Responding to Token Creation
- [protocol TKSmartCardTokenDriverDelegate](tksmartcardtokendriverdelegate.md)
  The interface that a smart card token driver delegate implements to respond to token creation events.

## Relationships

### Inherits From
- [TKTokenDriver](tktokendriver.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Authenticating Users with a Cryptographic Token](authenticating-users-with-a-cryptographic-token.md)
  Grant access to user accounts and the keychain by creating a smart card app extension.
- [Configuring Smart Card Authentication](configuring-smart-card-authentication.md)
  Set preferences for smart card authentication operations, including those on managed devices.
- [class TKSmartCardToken](tksmartcardtoken.md)
  A representation of a smart card based cryptographic token.
- [class TKSmartCardTokenSession](tksmartcardtokensession.md)
  A token session that is based on a smart card token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriver)*