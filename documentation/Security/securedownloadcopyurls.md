# SecureDownloadCopyURLs

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a list of URLs from which the data can be downloaded.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadCopyURLs(SecureDownloadRef downloadRef, CFArrayRef*urls);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

#### Discussion

The first URL in the list is the preferred download location. The other URLs are backup locations in case earlier locations in the list can’t be accessed.

## Parameters

- `downloadRef`: The secure download object to query.
- `urls`: A pointer to a [`CFArray`](../CoreFoundation/cfarray.md) object that the function sets to point at a new array containing one or more [`CFURL`](../CoreFoundation/cfurl.md) objects indicating the urls to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadcopyurls)*