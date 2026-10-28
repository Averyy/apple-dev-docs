# SecureDownloadCopyCreationDate

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns download ticket’s creation date.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadCopyCreationDate(SecureDownloadRef downloadRef, CFDateRef*date);
```

## Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `downloadRef`: The secure download to query.
- `date`: A pointer to a [`CFDate`](../CoreFoundation/cfdate.md) object that the function fills with the download’s creation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadcopycreationdate)*