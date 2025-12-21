# SecTrustCopyPublicKey(_:)

**Framework**: Security  
**Kind**: func

Returns the public key for a leaf certificate after it has been evaluated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecTrustCopyPublicKey(_ trust: SecTrust) -> SecKey?
```

## Mentions

- [Evaluating a Trust and Parsing the Result](evaluating-a-trust-and-parsing-the-result.md)
- [Getting an Existing Key](getting-an-existing-key.md)

#### Return Value

The leaf certificate’s public key, or `NULL` if it the public key could not be extracted (this can happen with DSA certificate chains if the parameters in the chain cannot be found). In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release this object when you are finished with it.

#### Discussion

Call the [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) function before calling this function.

When you call this function, it attempts to return the public key of the leaf certificate, even if the trust evaluation was unsuccessful. Even if the trust evaluation was successful, this function might still return `NULL`—for example, if the leaf certificate’s key can’t be extracted for some reason.

## Parameters

- `trust`: The trust management object for the certificate that has been evaluated.  Use the   function to create a trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopypublickey(_:))*