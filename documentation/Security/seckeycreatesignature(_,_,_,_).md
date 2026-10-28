# SecKeyCreateSignature(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates the cryptographic signature for a block of data using a private key and specified algorithm.

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
func SecKeyCreateSignature(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ dataToSign: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

```c
CFDataRefSecKeyCreateSignature(SecKeyRef key, SecKeyAlgorithm algorithm, CFDataRef dataToSign, CFErrorRef*error);
```

## Mentions

- [Signing and Verifying](./signing-and-verifying.md)

## Return Value

The digital signature or `NULL` on failure. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the data’s memory when you are done with it.

## Discussion

You later evaluate the combined data and signature with the corresponding public key and a call to the [`SecKeyVerifySignature(_:_:_:_:_:)`](./seckeyverifysignature%28_,_,_,_,_%29.md) function.

## Parameters

- `key`: The private key to use in creating the signature.
- `algorithm`: The signing algorithm to use. Use one of the signing algorithms listed in [`SecKeyAlgorithm`](./seckeyalgorithm.md). You can use the [`SecKeyIsAlgorithmSupported(_:_:_:)`](./seckeyisalgorithmsupported%28_,_,_%29.md) function to test that the key is suitable for the algorithm.
- `dataToSign`: The data whose signature you want.
- `error`: The address of a [`CFError`](../CoreFoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatesignature(_:_:_:_:))*