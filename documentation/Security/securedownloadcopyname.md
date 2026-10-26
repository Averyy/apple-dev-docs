# SecureDownloadCopyName

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the printable name of the download ticket.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadCopyName(SecureDownloadRef downloadRef, CFStringRef*name);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `downloadRef`: The secure download to query.
- `name`: A pointer to a CFStringRef object that the function fills with the secure download’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadcopyname)*