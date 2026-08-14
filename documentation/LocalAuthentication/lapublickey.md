# LAPublicKey

**Framework**: Local Authentication  
**Kind**: class

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

## Topics

### Checking algorithm support
- [func canEncrypt(using: SecKeyAlgorithm) -> Bool](lapublickey/canencrypt(using:).md)
  Checks whether the algorithm you supply is valid for encrypting data with the key.
- [func canVerify(using: SecKeyAlgorithm) -> Bool](lapublickey/canverify(using:).md)
  Checks whether the algorithm you supply is valid for verifying signatures with the key.
### Performing cryptographic operations
- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](lapublickey/encrypt(_:algorithm:completion:).md)
  Encrypts the data you supply with a given algorithm.
- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](lapublickey/exportbytes(completion:).md)
  Exports the data that represents a public key.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](lapublickey/verify(_:signature:algorithm:completion:).md)
  Verifies a digital signature for the data you supply.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class LAPrivateKey](laprivatekey.md)
  The private portion of an asymmetric key pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey)*