# keychainContents

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The contents of the keychain for this token.

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
var keychainContents: TKTokenKeychainContents? { get }
```

```objc
@property (readonly, nullable) TKTokenKeychainContents * keychainContents;
```

## See Also

### Accessing Keychain Items
- [class TKTokenKeychainContents](../tktokenkeychaincontents.md)
  A representation of the state of the keychain for a particular token.
- [class TKTokenKeychainItem](../tktokenkeychainitem.md)
  An abstract base class for managing a token’s contents as keychain items.
- [class TKTokenKeychainCertificate](../tktokenkeychaincertificate.md)
  A token’s certificate as stored in the keychain.
- [class TKTokenKeychainKey](../tktokenkeychainkey.md)
  A token’s key as stored in the keychain.
- [typealias ObjectID](./objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](./objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/keychaincontents)*