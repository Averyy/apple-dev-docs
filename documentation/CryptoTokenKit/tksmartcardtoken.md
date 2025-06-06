# TKSmartCardToken

**Framework**: CryptoTokenKit  
**Kind**: class

A representation of a smart card based cryptographic token.

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
class TKSmartCardToken
```

## Mentions

- [Authenticating Users with a Cryptographic Token](authenticating-users-with-a-cryptographic-token.md)

## Topics

### Creating Smart Card Tokens
- [init(smartCard: TKSmartCard, aid: Data?, instanceID: String, tokenDriver: TKSmartCardTokenDriver)](tksmartcardtoken/init(smartcard:aid:instanceid:tokendriver:).md)
  Initializes a smart card token with the specified smart card, application identifier, and token driver.
### Accessing the Application Identifier
- [var aid: Data?](tksmartcardtoken/aid.md)
  The ISO 7816-4 application identifiers of the Smart Card.
### Accessing Smart Cards
- [class TKSmartCard](tksmartcard.md)
  A representation of a smart card.
### Working with Tag-Length-Value Records
- [class TKTLVRecord](tktlvrecord.md)
  The base class encapsulating a Tag-Length-Value record.
- [class TKBERTLVRecord](tkbertlvrecord.md)
  An object that parses BER-encoded data and produces DER-encoded data for TLV records.
- [class TKCompactTLVRecord](tkcompacttlvrecord.md)
  An object that implements encoding using Compact-TLV encoding according to ISO 7816-4.
- [class TKSimpleTLVRecord](tksimpletlvrecord.md)
  An object that implements encoding using Simple-TLV encoding according to ISO 7816-4.

## Relationships

### Inherits From
- [TKToken](tktoken.md)
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
- [class TKSmartCardTokenDriver](tksmartcardtokendriver.md)
  The driver that acts as an entry point for smart card app extensions.
- [class TKSmartCardTokenSession](tksmartcardtokensession.md)
  A token session that is based on a smart card token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken)*