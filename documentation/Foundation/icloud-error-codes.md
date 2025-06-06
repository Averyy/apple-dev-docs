# iCloud Error Codes

**Framework**: Foundation

Error codes to expect when an iCloud-related error occurs.

#### Overview

These codes are associated with the [`ubiquitousItemDownloadingErrorKey`](urlresourcekey/ubiquitousitemdownloadingerrorkey.md) on an [`NSURL`](nsurl.md) object when an iCloud-related error occurs.

## Topics

### General iCloud File Errors
- [var NSUbiquitousFileErrorMinimum: Int](nsubiquitousfileerrorminimum-swift.var.md)
  The minimum error code value that represents an iCloud error.
- [var NSUbiquitousFileUnavailableError: Int](nsubiquitousfileunavailableerror-swift.var.md)
  The item has not been uploaded to iCloud by another device yet.
- [var NSUbiquitousFileNotUploadedDueToQuotaError: Int](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md)
  The item could not be uploaded to iCloud because it would make the account go over its quota.
- [var NSUbiquitousFileUbiquityServerNotAvailable: Int](nsubiquitousfileubiquityservernotavailable-swift.var.md)
  A failure to connect to the iCloud servers.
- [var NSUbiquitousFileErrorMaximum: Int](nsubiquitousfileerrormaximum-swift.var.md)
  The maximum error code value that represents an iCloud error.
### iCloud Sharing Errors
- [var NSCloudSharingConflictError: Int](nscloudsharingconflicterror-swift.var.md)
  A conflict occurred during an attempt to save changes.
- [var NSCloudSharingErrorMaximum: Int](nscloudsharingerrormaximum-swift.var.md)
  The end of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingErrorMinimum: Int](nscloudsharingerrorminimum-swift.var.md)
  The start of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingNetworkFailureError: Int](nscloudsharingnetworkfailureerror-swift.var.md)
  Sharing failed due to a network failure.
- [var NSCloudSharingNoPermissionError: Int](nscloudsharingnopermissionerror-swift.var.md)
  The current user doesn’t have permission to perform the requested actions.
- [var NSCloudSharingOtherError: Int](nscloudsharingothererror-swift.var.md)
  An otherwise unspecified cloud-sharing error occurred.
- [var NSCloudSharingQuotaExceededError: Int](nscloudsharingquotaexceedederror-swift.var.md)
  The user doesn’t have enough storage space available to share the requested items.
- [var NSCloudSharingTooManyParticipantsError: Int](nscloudsharingtoomanyparticipantserror-swift.var.md)
  Additional participants couldn’t be added to the share, because the limit was reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/icloud-error-codes)*