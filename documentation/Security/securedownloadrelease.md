# SecureDownloadRelease

**Framework**: Security  
**Kind**: func  
**Role**: Function

Releases the memory associated with a secure download object.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadRelease(SecureDownloadRef downloadRef);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `downloadRef`: The secure download object to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadrelease)*