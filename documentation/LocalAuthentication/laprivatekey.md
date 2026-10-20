# LAPrivateKey

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

The private portion of an asymmetric key pair.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LAPrivateKey
```

```objc
@interface LAPrivateKey : NSObject
```

## Topics

### Accessing the associated public key
- [var publicKey: LAPublicKey](./laprivatekey/publickey.md)
  The public key that corresponds with the private key in a key pair.
### Checking algorithm support
- [func canDecrypt(using: SecKeyAlgorithm) -> Bool](./laprivatekey/candecrypt%28using%29.md)
  Checks whether the algorithm you supply is valid for decrypting data with the key.
- [func canExchangeKeys(using: SecKeyAlgorithm) -> Bool](./laprivatekey/canexchangekeys%28using%29.md)
  Checks whether the algorithm you supply is valid for performing key exchanges.
- [func canSign(using: SecKeyAlgorithm) -> Bool](./laprivatekey/cansign%28using%29.md)
  Checks whether the algorithm you supply is valid for signing data with the key.
### Performing cryptographic operations
- [func decrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./laprivatekey/decrypt%28_,algorithm,completion%29.md)
  Decrypts the data you supply with a given algorithm.
- [func exchangeKeys(publicKey: Data, algorithm: SecKeyAlgorithm, parameters: [AnyHashable : Any], completion: (Data?, (any Error)?) -> Void)](./laprivatekey/exchangekeys%28publickey,algorithm,parameters,completion%29.md)
  Performs a Diffie-Hellman style key exchange operation.
- [func sign(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./laprivatekey/sign%28_,algorithm,completion%29.md)
  Generates a digital signature for the data you supply.

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

### Key pairs
- [class LAPublicKey](./lapublickey.md)
  The public portion of an asymmetric key pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey)*