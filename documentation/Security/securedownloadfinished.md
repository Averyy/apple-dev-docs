# SecureDownloadFinished

**Framework**: Security  
**Kind**: func  
**Role**: Function

Concludes the secure download process.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadFinished(SecureDownloadRef downloadRef);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

#### Discussion

Call this after all data has been received.

## Parameters

- `downloadRef`: The secure download object to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadfinished)*