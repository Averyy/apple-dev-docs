# TKTokenKeychainKey

**Framework**: CryptoTokenKit  
**Kind**: class

A token’s key as stored in the keychain.

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
class TKTokenKeychainKey
```

## Topics

### Creating Token Keychain Keys
- [init?(certificate: SecCertificate?, objectID: TKToken.ObjectID)](tktokenkeychainkey/init(certificate:objectid:).md)
  Initializes a token keychain key with data from the specified certificate reference and a given object ID.
### Accessing Key Attributes
- [var keyType: String](tktokenkeychainkey/keytype.md)
  The type of the key. Currently, only [`kSecAttrKeyTypeRSA`](https://developer.apple.com/documentation/Security/kSecAttrKeyTypeRSA) and `kSecAttrKeyTypeECSECPrimeRandom` are supported values.
- [var keySizeInBits: Int](tktokenkeychainkey/keysizeinbits.md)
- [var applicationTag: Data?](tktokenkeychainkey/applicationtag.md)
  The private tag data.
- [var publicKeyData: Data?](tktokenkeychainkey/publickeydata.md)
  The public key data.
- [var publicKeyHash: Data?](tktokenkeychainkey/publickeyhash.md)
  The SHA1 hash of the raw public key.
- [var canDecrypt: Bool](tktokenkeychainkey/candecrypt.md)
  Whether the key can be used to decrypt data.
- [var canSign: Bool](tktokenkeychainkey/cansign.md)
  Whether the key can be used to sign data.
- [var canPerformKeyExchange: Bool](tktokenkeychainkey/canperformkeyexchange.md)
  Whether the key can be used to perform Diffie-Hellman style cryptographic key exchange.
- [var isSuitableForLogin: Bool](tktokenkeychainkey/issuitableforlogin.md)
  Whether the key can be used for system login.

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
- [class TKTokenKeychainCertificate](tktokenkeychaincertificate.md)
  A token’s certificate as stored in the keychain.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey)*