# SecTrustGetTPHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the trust policy handle.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecTrustGetTPHandle(SecTrustRef trust, CSSM_TP_HANDLE *handle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

The trust policy handle is the CSSM identifier of the trust policy module that is managing the certificate. The trust policy handle is used as an input to a number of CSSM functions.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [`SecTrustSetVerifyDate(_:_:)`](./sectrustsetverifydate%28_,_%29.md) function for the same trust management object on another thread.

## Parameters

- `trust`: The trust management object from which to obtain the trust policy handle. A trust management object includes one or more certificates plus the policy or policies to be used in evaluating trust. Use the [`SecTrustCreateWithCertificates(_:_:_:)`](./sectrustcreatewithcertificates%28_,_,_%29.md) function to create a trust management object.
- `handle`: On return, points to a CSSM trust policy handle. This handle remains valid until the trust management object is released or until the next call to the function [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) that uses this trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgettphandle)*