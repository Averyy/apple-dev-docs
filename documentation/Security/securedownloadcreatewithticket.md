# SecureDownloadCreateWithTicket

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a secure download object for use during the download process.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadCreateWithTicket(CFDataRef ticket, SecureDownloadTrustSetupCallback setup, void *setupContext, SecureDownloadTrustEvaluateCallback evaluate, void *evaluateContext, SecureDownloadRef*downloadRef);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `ticket`: The download ticket.
- `setup`: A pointer to a function that Secure Download calls before trust is verified for each signer of the ticket. This allows you to modify the [`SecTrust`](./sectrust.md) if needed.  The callback returns a [`SecureDownloadTrustCallbackResult`](./securedownloadtrustcallbackresult.md).
- `setupContext`: An arbitrary context passed to the `setup` callback.
- `evaluate`: A pointer to a function that Secure Download calls after calling [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) for a signer if the result was not trusted. This allows you to query the user as to whether or not to trust the signer by returning a [`SecTrustResultType`](./sectrustresulttype.md) value.
- `evaluateContext`: An arbitrary context passed to the `evaluate` callback.
- `downloadRef`: A pointer that is set to the new download reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadcreatewithticket)*