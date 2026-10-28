# SecTrustGetCssmResultCode

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the CSSM result code from the most recent trust evaluation for a trust management object.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecTrustGetCssmResultCode(SecTrustRef trust, OSStatus *resultCode);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). Returns [`errSecTrustNotAvailable`](./errsectrustnotavailable.md) if the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function has not been called for the specified trust.

## Discussion

Whereas the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function returns one of the Security Framework result codes (see [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)), the `SecTrustGetCssmResultCode` function returns the CSSM result code as enumerated in `Security.framework/cssmerr.h`. Call this function to get a more specific reason for a failure than provided by `SecTrustEvaluate`. Other functions that might be of interest are the [`SecTrustGetTrustResult(_:_:)`](./sectrustgettrustresult%28_,_%29.md) function, which returns detailed results for each certificate in the certificate chain, and the [`SecTrustGetCssmResult`](./sectrustgetcssmresult.md) function, which returns the results in a format that can be passed directly to CSSM functions.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [`SecTrustSetVerifyDate(_:_:)`](./sectrustsetverifydate%28_,_%29.md) function for the same trust management object on another thread.

## Parameters

- `trust`: The trust management object for which you wish to retrieve a result code.
- `resultCode`: On return, the CSSM result code produced by the most recent call to the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function for the trust management object specified in the `trust` parameter.  The value of this parameter is undefined if `SecTrustEvaluate` has not been called.

## See Also

### Related Documentation
- [func SecTrustGetTrustResult(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](./sectrustgettrustresult%28_,_%29.md)
  Returns the result code from the most recent trust evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgetcssmresultcode)*