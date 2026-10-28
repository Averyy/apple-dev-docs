# SecTrustGetResult

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves details on the outcome of a call to the function `SecTrustEvaluate`.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecTrustGetResult(SecTrustRef trustRef, SecTrustResultType *result, CFArrayRef*certChain, CSSM_TP_APPLE_EVIDENCE_INFO **statusChain);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

After calling the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function, you can call the [`SecTrustGetResult`](./sectrustgetresult.md) function or the [`SecTrustGetCssmResult`](./sectrustgetcssmresult.md) function to get detailed information about the results of the evaluation. Whereas the `SecTrustGetResult` function returns the information in a form that you can interpret without extensive knowledge of CSSM, the [`SecTrustGetCssmResult`](./sectrustgetcssmresult.md) function returns information in a form that can be passed directly to CSSM functions.

You can call the `SFCertificateTrustPanel` class in the [Security Interface](../SecurityInterface/SecurityInterface.md) to display these results to the user.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [`SecTrustSetVerifyDate(_:_:)`](./sectrustsetverifydate%28_,_%29.md) function for the same trust management object on another thread.

### Special Considerations

Use [`SecTrustGetTrustResult(_:_:)`](./sectrustgettrustresult%28_,_%29.md) for new development instead.

## Parameters

- `trustRef`: A trust management object that has previously been sent to the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function for evaluation.
- `result`: A pointer to the result type returned in the `result` parameter by the `SecTrustEvaluate` function.
- `certChain`: On return, points to an array of certificates that constitute the certificate chain used to verify the input certificate. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.
- `statusChain`: On return, points to an array of `CSSM_TP_APPLE_EVIDENCE_INFO` structures, one for each certificate in the certificate chain. The first item in the array corresponds to the leaf certificate, and the last item corresponds to the anchor (assuming that verification of the chain did not fail before reaching the anchor certificate). Each structure describes the status of one certificate in the chain. This structure is defined in `cssmapple.h`. Do not attempt to free this pointer; it remains valid until the trust management object is released or until the next call to the function `SecTrustEvaluate` that uses this trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgetresult)*