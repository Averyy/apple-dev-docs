# TKToken.ObjectID

**Framework**: CryptoTokenKit  
**Kind**: typealias

A unique and persistent identifier of a particular token object.

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
typealias ObjectID = Any
```

#### Discussion

The type of this identifier must support property list serialization and must define its format by the implementation of the token extension.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/objectid)*