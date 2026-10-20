# TKTokenKeyAlgorithm

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

Cryptographic algorithms used by token keys.

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
class TKTokenKeyAlgorithm
```

```objc
@interface TKTokenKeyAlgorithm : NSObject
```

#### Overview

Typically, the supported algorithm for a token key can be represented by a value of the `SecKeyAlgorithm` enumeration. However, tokens such as Smart Cards require that input data for operations take the format of a more specific algorithm. For example, a token may accept raw data to generate a cryptographic signature, but require that raw data to be formatted according to PKCS1 padding rules. To express such a requirement, a `TKTokenKeyAlgorithm` object defines a target algorithm and a set of other algorithms that were used. In the previous example, the target algorithm is `kSecKeyAlgorithmRSASignatureRaw` and the `kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA1` algorithm is also reported as being  used.

## Topics

### Determining Algorithm Usage
- [func isAlgorithm(SecKeyAlgorithm) -> Bool](./tktokenkeyalgorithm/isalgorithm%28_%29.md)
  Returns whether the specified algorithm is the target operation algorithm.
- [func supportsAlgorithm(SecKeyAlgorithm) -> Bool](./tktokenkeyalgorithm/supportsalgorithm%28_%29.md)
  Whether the specified algorithm is the target operation algorithm, or one of the other algorithms used.

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

### Determining Support for Operations
- [func tokenSession(TKTokenSession, supports: TKTokenOperation, keyObjectID: TKToken.ObjectID, algorithm: TKTokenKeyAlgorithm) -> Bool](./tktokensessiondelegate/tokensession%28_,supports,keyobjectid,algorithm%29.md)
  Asks the delegate whether the token session supports a given operation using the specified key and algorithm.
- [enum TKTokenOperation](./tktokenoperation.md)
  Operations that can be performed with a token’s keys and certificates.
- [typealias ObjectID](./tktoken/objectid.md)
  A unique and persistent identifier of a particular token object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm)*