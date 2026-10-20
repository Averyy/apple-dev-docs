# LAPublicKey

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

The public portion of an asymmetric key pair.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LAPublicKey
```

```objc
@interface LAPublicKey : NSObject
```

## Topics

### Checking algorithm support
- [func canEncrypt(using: SecKeyAlgorithm) -> Bool](./lapublickey/canencrypt%28using%29.md)
  Checks whether the algorithm you supply is valid for encrypting data with the key.
- [func canVerify(using: SecKeyAlgorithm) -> Bool](./lapublickey/canverify%28using%29.md)
  Checks whether the algorithm you supply is valid for verifying signatures with the key.
### Performing cryptographic operations
- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./lapublickey/encrypt%28_,algorithm,completion%29.md)
  Encrypts the data you supply with a given algorithm.
- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](./lapublickey/exportbytes%28completion%29.md)
  Exports the data that represents a public key.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](./lapublickey/verify%28_,signature,algorithm,completion%29.md)
  Verifies a digital signature for the data you supply.

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
- [class LAPrivateKey](./laprivatekey.md)
  The private portion of an asymmetric key pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey)*