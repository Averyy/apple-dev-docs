# TKTokenKeychainCertificate

**Framework**: CryptoTokenKit  
**Kind**: class

A token’s certificate as stored in the keychain.

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
class TKTokenKeychainCertificate
```

## Topics

### Creating Token Keychain Certificates
- [init?(certificate: SecCertificate, objectID: TKToken.ObjectID)](tktokenkeychaincertificate/init(certificate:objectid:).md)
  Initializes a token keychain certificate with data from the specified certificate reference and a given object ID.
### Accessing Certificate Data
- [var data: Data](tktokenkeychaincertificate/data.md)
  Returns a DER-encoded representation of an X.509 certificate.

## Relationships

### Inherits From
- [TKTokenKeychainItem](tktokenkeychainitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var keychainContents: TKTokenKeychainContents?](tktoken/keychaincontents.md)
  The contents of the keychain for this token.
- [class TKTokenKeychainContents](tktokenkeychaincontents.md)
  A representation of the state of the keychain for a particular token.
- [class TKTokenKeychainItem](tktokenkeychainitem.md)
  An abstract base class for managing a token’s contents as keychain items.
- [class TKTokenKeychainKey](tktokenkeychainkey.md)
  A token’s key as stored in the keychain.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate)*