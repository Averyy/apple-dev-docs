# Secure Download

**Framework**: Security  
**Role**: API Collection

Implement Apple’s Secure Download System in macOS.

## Overview

The `Security.SecureDownload` API provides access to Apple’s Secure Download System. This API is only useful for certain specialized apps. Because of this, you must import this API explicitly:

```objc
#import <Security/SecureDownload.h>
```

## Topics

### Result Codes
- [Secure Download Result Codes](./secure-download-result-codes.md)
  Result codes specific to the secure download API.
### Download Creation
- [SecureDownloadCreateWithTicket](./securedownloadcreatewithticket.md)
  Creates a secure download object for use during the download process.
- [SecureDownloadTrustEvaluateCallback](./securedownloadtrustevaluatecallback.md)
  Optionally queries the user how to handle a failed trust evaluation.
- [SecureDownloadTrustSetupCallback](./securedownloadtrustsetupcallback.md)
  Determines whether trust for a particular signer should be evaluated.
- [SecureDownloadTrustCallbackResult](./securedownloadtrustcallbackresult.md)
  A flag used to indicate whether or not a signer should be evaluated.
- [SecureDownloadRef](./securedownloadref.md)
  An opaque type representing a secure download object.
### Download Settings
- [SecureDownloadGetDownloadSize](./securedownloadgetdownloadsize.md)
  Returns the size of the expected download.
- [SecureDownloadCopyCreationDate](./securedownloadcopycreationdate.md)
  Returns download ticket’s creation date.
- [SecureDownloadCopyName](./securedownloadcopyname.md)
  Returns the printable name of the download ticket.
- [SecureDownloadCopyTicketLocation](./securedownloadcopyticketlocation.md)
  Copies the ticket location from a secure download URL.
- [SecureDownloadCopyURLs](./securedownloadcopyurls.md)
  Returns a list of URLs from which the data can be downloaded.
### Receiving Data
- [SecureDownloadUpdateWithData](./securedownloadupdatewithdata.md)
  Checks data received during download for validity.
### Download Completion
- [SecureDownloadFinished](./securedownloadfinished.md)
  Concludes the secure download process.
- [SecureDownloadRelease](./securedownloadrelease.md)
  Releases the memory associated with a secure download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secure-download)*