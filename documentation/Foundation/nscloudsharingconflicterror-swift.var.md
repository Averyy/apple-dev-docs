# NSCloudSharingConflictError

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A conflict occurred during an attempt to save changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var NSCloudSharingConflictError: Int { get }
```

#### Discussion

This error occurs when a conflict is detected while trying to save changes to the [`CKShare`](../CloudKit/ckshare.md) or root [`CKRecord`](../CloudKit/ckrecord.md). Respond to this error by first fetching the server’s changes to the records, then either handle the conflict manually or present it, which will instruct the user to try the operation again.

## See Also

### iCloud Sharing Errors
- [var NSCloudSharingErrorMaximum: Int](./nscloudsharingerrormaximum-swift.var.md)
  The end of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingErrorMinimum: Int](./nscloudsharingerrorminimum-swift.var.md)
  The start of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingNetworkFailureError: Int](./nscloudsharingnetworkfailureerror-swift.var.md)
  Sharing failed due to a network failure.
- [var NSCloudSharingNoPermissionError: Int](./nscloudsharingnopermissionerror-swift.var.md)
  The current user doesn’t have permission to perform the requested actions.
- [var NSCloudSharingOtherError: Int](./nscloudsharingothererror-swift.var.md)
  An otherwise unspecified cloud-sharing error occurred.
- [var NSCloudSharingQuotaExceededError: Int](./nscloudsharingquotaexceedederror-swift.var.md)
  The user doesn’t have enough storage space available to share the requested items.
- [var NSCloudSharingTooManyParticipantsError: Int](./nscloudsharingtoomanyparticipantserror-swift.var.md)
  Additional participants couldn’t be added to the share, because the limit was reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscloudsharingconflicterror-swift.var)*