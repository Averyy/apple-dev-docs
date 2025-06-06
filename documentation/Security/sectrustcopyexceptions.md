# SecTrustCopyExceptions(_:)

**Framework**: Security  
**Kind**: func

Returns an opaque cookie containing exceptions to trust policies that will allow future evaluations of the current certificate to succeed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustCopyExceptions(_ trust: SecTrust) -> CFData?
```

#### Return Value

An opaque cookie. If you pass this cookie to [`SecTrustSetExceptions(_:_:)`](sectrustsetexceptions(_:_:).md), that function sets a list of exceptions for future processing of the certificate. Once this list of exceptions are set, a subsequent call to [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) for that certificate will return `true`.

#### Discussion

Note: If a new error occurs that did not occur when this function was called originally, the subsequent call to [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) can still fail. For example, if the certificate expires between calling `SecTrustCopyExceptions` and [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md), evaluation will fail.

#### Discussion

Normally this API should only be called after asking the user how to proceed, and even then, only if the user explicitly tells your application to trust the current certificate chain in spite of the errors presented.

## Parameters

- `trust`: The evaluated trust management object whose policies you wish to retrieve.

## See Also

- [func SecTrustSetPolicies(SecTrust, CFTypeRef) -> OSStatus](sectrustsetpolicies(_:_:).md)
  Sets the policies to use in an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopyexceptions(_:))*