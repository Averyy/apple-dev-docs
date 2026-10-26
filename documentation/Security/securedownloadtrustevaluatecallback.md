# SecureDownloadTrustEvaluateCallback

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

Optionally queries the user how to handle a failed trust evaluation.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
typedef enum SecTrustResultType (*)(struct __SecTrust *, enum SecTrustResultType, void *) SecureDownloadTrustEvaluateCallback;
```

#### Return Value

A trust evaluation result.

## Parameters

- `trustRef`: The trust used for this evaluation.
- `result`: The result of the trust evaluation.
- `evaluateContext`: An arbitrary value that you passed in as the `evaluateContext` parameter to the [`SecureDownloadCreateWithTicket`](./securedownloadcreatewithticket.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadtrustevaluatecallback)*