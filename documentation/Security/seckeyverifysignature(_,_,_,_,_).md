# SecKeyVerifySignature(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Verifies the cryptographic signature of a block of data using a public key and specified algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SecKeyVerifySignature(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ signedData: CFData, _ signature: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

```c
Boolean SecKeyVerifySignature(SecKeyRef key, SecKeyAlgorithm algorithm, CFDataRef signedData, CFDataRef signature, CFErrorRef*error);
```

## Mentions

- [Signing and Verifying](./signing-and-verifying.md)

## Return Value

A Boolean indicating whether or not the data and signature are intact.

## Parameters

- `key`: The public key to use in evaluating the signature.
- `algorithm`: The algorithm that was used to create the signature. Use one of the signing algorithms listed in [`SecKeyAlgorithm`](./seckeyalgorithm.md). You can use the [`SecKeyIsAlgorithmSupported(_:_:_:)`](./seckeyisalgorithmsupported%28_,_,_%29.md) function to test that the key is suitable for the algorithm.
- `signedData`: The data that was signed.
- `signature`: The signature that was created with a call to the [`SecKeyCreateSignature(_:_:_:_:)`](./seckeycreatesignature%28_,_,_,_%29.md) function.
- `error`: The address of a [`CFError`](../CoreFoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyverifysignature(_:_:_:_:_:))*