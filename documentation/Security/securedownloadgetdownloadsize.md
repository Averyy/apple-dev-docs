# SecureDownloadGetDownloadSize

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the size of the expected download.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadGetDownloadSize(SecureDownloadRef downloadRef, SInt64 *downloadSize);
```

## Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `downloadRef`: The secure download object to query.
- `downloadSize`: A pointer that the function fills with the the download size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadgetdownloadsize)*