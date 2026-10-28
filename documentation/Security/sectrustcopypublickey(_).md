# SecTrustCopyPublicKey(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the public key for a leaf certificate after it has been evaluated.

**Availability**:
- iOS 2.0+ - Deprecated in 14.0 (renamed: SecTrustCopyKey(_:))
- iPadOS 2.0+ - Deprecated in 14.0 (renamed: SecTrustCopyKey(_:))
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: SecTrustCopyKey(_:))
- macOS 10.7+ - Deprecated in 11.0 (renamed: SecTrustCopyKey(_:))
- tvOS 9.0+ - Deprecated in 14.0 (renamed: SecTrustCopyKey(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecTrustCopyKey(_:))
- watchOS 1.0+ - Deprecated in 7.0 (renamed: SecTrustCopyKey(_:))

## Declaration

```swift
func SecTrustCopyPublicKey(_ trust: SecTrust) -> SecKey?
```

```c
SecKeyRefSecTrustCopyPublicKey(SecTrustRef trust);
```

## Mentions

- [Evaluating a Trust and Parsing the Result](./evaluating-a-trust-and-parsing-the-result.md)
- [Getting an Existing Key](./getting-an-existing-key.md)

## Return Value

The leaf certificate’s public key, or `NULL` if it the public key could not be extracted (this can happen with DSA certificate chains if the parameters in the chain cannot be found). In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.

## Discussion

Call the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function before calling this function.

When you call this function, it attempts to return the public key of the leaf certificate, even if the trust evaluation was unsuccessful. Even if the trust evaluation was successful, this function might still return `NULL`—for example, if the leaf certificate’s key can’t be extracted for some reason.

## Parameters

- `trust`: The trust management object for the certificate that has been evaluated.  Use the [`SecTrustCreateWithCertificates(_:_:_:)`](./sectrustcreatewithcertificates%28_,_,_%29.md) function to create a trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopypublickey(_:))*