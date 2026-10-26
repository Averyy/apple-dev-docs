# SecureDownloadCopyTicketLocation

**Framework**: Security  
**Kind**: func  
**Role**: Function

Copies the ticket location from a secure download URL.

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecureDownloadCopyTicketLocation(CFURLRef url, CFURLRef*ticketLocation);
```

#### Return Value

A result code. See [Secure Download Result Codes](./secure-download-result-codes.md).

## Parameters

- `url`: A secure download URL.
- `ticketLocation`: A pointer to a [`CFURL`](../CoreFoundation/cfurl.md) object that the function fills with the URL of the ticket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/securedownloadcopyticketlocation)*