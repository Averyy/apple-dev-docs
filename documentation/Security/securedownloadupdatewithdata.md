# SecureDownloadUpdateWithData

**Framework**: Security  
**Kind**: func  
**Role**: Function

Checks data received during download for validity.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadUpdateWithData(SecureDownloadRef downloadRef, CFDataRef data);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md). If the data is invalid, the result code is `enum (unnamed)-3yczz/errSecureDownloadInvalidDownload`.

#### Discussion

Call this function each time data is received.

## Parameters

- `downloadRef`: The secure download object to query.
- `data`: The data to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadupdatewithdata)*