# TKTokenKeychainItem

**Framework**: CryptoTokenKit  
**Kind**: class

An abstract base class for managing a token’s contents as keychain items.

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
class TKTokenKeychainItem
```

#### Overview

Don’t use this base class directly. Instead, use one of its subclasses, such as [`TKTokenKeychainCertificate`](tktokenkeychaincertificate.md) for managing certificates or [`TKTokenKeychainKey`](tktokenkeychainkey.md) for managing cryptographic keys.

## Topics

### Creating Token Keychain Items
- [init(objectID: TKToken.ObjectID)](tktokenkeychainitem/init(objectid:).md)
  Initializes a token keychain item with the specified object ID.
### Accessing Keychain Item Attributes
- [var objectID: TKToken.ObjectID](tktokenkeychainitem/objectid.md)
  Returns the object ID used for keychain item identification.
- [var label: String?](tktokenkeychainitem/label.md)
  The user-visible label for the keychain item.
- [var constraints: [NSNumber : Any]?](tktokenkeychainitem/constraints.md)
  Access constraints for the keychain item, keyed by [`TKTokenOperation`](tktokenoperation.md) values wrapped in [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKTokenKeychainCertificate](tktokenkeychaincertificate.md)
- [TKTokenKeychainKey](tktokenkeychainkey.md)
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
- [class TKTokenKeychainCertificate](tktokenkeychaincertificate.md)
  A token’s certificate as stored in the keychain.
- [class TKTokenKeychainKey](tktokenkeychainkey.md)
  A token’s key as stored in the keychain.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.
- [typealias ObjectID](tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem)*