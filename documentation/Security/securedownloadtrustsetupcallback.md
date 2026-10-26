# SecureDownloadTrustSetupCallback

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

Determines whether trust for a particular signer should be evaluated.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
typedef enum _SecureDownloadTrustCallbackResult (*)(struct __SecTrust *, void *) SecureDownloadTrustSetupCallback;
```

#### Return Value

A trust callback result that indicates whether or not a signer should be evaluated.

## Parameters

- `trustRef`: The trust used for this evaluation.
- `setupContext`: An arbitrary value that you passed in as the `setupContext` parameter to the [`SecureDownloadCreateWithTicket`](./securedownloadcreatewithticket.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadtrustsetupcallback)*