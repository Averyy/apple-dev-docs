# NSUbiquitousFileUnavailableError

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

The item has not been uploaded to iCloud by another device yet.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
NSUbiquitousFileUnavailableError
```

#### Discussion

When this error occurs, you do not need to ask the system to start downloading the item. The system will download the item as soon as it can. If you want to know when the item becomes available, use an [`NSMetadataQuery`](./nsmetadataquery.md) object to monitor changes to the file’s URL.

## See Also

### General iCloud File Errors
- [NSUbiquitousFileErrorMinimum](./nsubiquitousfileerrorminimum-c.enum.case.md)
  The minimum error code value that represents an iCloud error.
- [NSUbiquitousFileNotUploadedDueToQuotaError](./nsubiquitousfilenotuploadedduetoquotaerror-c.enum.case.md)
  The item could not be uploaded to iCloud because it would make the account go over its quota.
- [NSUbiquitousFileUbiquityServerNotAvailable](./nsubiquitousfileubiquityservernotavailable-c.enum.case.md)
  A failure to connect to the iCloud servers.
- [NSUbiquitousFileErrorMaximum](./nsubiquitousfileerrormaximum-c.enum.case.md)
  The maximum error code value that represents an iCloud error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitousfileunavailableerror-c.enum.case)*