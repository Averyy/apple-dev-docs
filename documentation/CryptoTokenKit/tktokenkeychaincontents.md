# TKTokenKeychainContents

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A representation of the state of the keychain for a particular token.

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
class TKTokenKeychainContents
```

```objc
@interface TKTokenKeychainContents : NSObject
```

## Topics

### Adding Keychain Items
- [func fill(with: [TKTokenKeychainItem])](./tktokenkeychaincontents/fill%28with%29.md)
  Fills the keychain with the specified items.
### Accessing Keychain Items
- [var items: [TKTokenKeychainItem]](./tktokenkeychaincontents/items.md)
  Returns all items for token in the keychain.
- [func key(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainKey](./tktokenkeychaincontents/key%28forobjectid%29.md)
  Returns the key for a specified object identifier.
- [func certificate(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](./tktokenkeychaincontents/certificate%28forobjectid%29.md)
  Returns the key for a specified object identifier.

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

## See Also

### Accessing Keychain Items
- [var keychainContents: TKTokenKeychainContents?](./tktoken/keychaincontents.md)
  The contents of the keychain for this token.
- [class TKTokenKeychainItem](./tktokenkeychainitem.md)
  An abstract base class for managing a token’s contents as keychain items.
- [class TKTokenKeychainCertificate](./tktokenkeychaincertificate.md)
  A token’s certificate as stored in the keychain.
- [class TKTokenKeychainKey](./tktokenkeychainkey.md)
  A token’s key as stored in the keychain.
- [typealias ObjectID](./tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](./tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents)*