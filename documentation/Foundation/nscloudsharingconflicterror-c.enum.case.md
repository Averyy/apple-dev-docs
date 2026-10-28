# NSCloudSharingConflictError

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

A conflict occurred during an attempt to save changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```c
NSCloudSharingConflictError
```

## Discussion

This error occurs when a conflict is detected while trying to save changes to the [`CKShare`](../CloudKit/ckshare.md) or root [`CKRecord`](../CloudKit/ckrecord.md). Respond to this error by first fetching the server’s changes to the records, then either handle the conflict manually or present it, which will instruct the user to try the operation again.

## See Also

### iCloud Sharing Errors
- [NSCloudSharingErrorMaximum](./nscloudsharingerrormaximum-c.enum.case.md)
  The end of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingErrorMinimum](./nscloudsharingerrorminimum-c.enum.case.md)
  The start of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingNetworkFailureError](./nscloudsharingnetworkfailureerror-c.enum.case.md)
  Sharing failed due to a network failure.
- [NSCloudSharingNoPermissionError](./nscloudsharingnopermissionerror-c.enum.case.md)
  The current user doesn’t have permission to perform the requested actions.
- [NSCloudSharingOtherError](./nscloudsharingothererror-c.enum.case.md)
  An otherwise unspecified cloud-sharing error occurred.
- [NSCloudSharingQuotaExceededError](./nscloudsharingquotaexceedederror-c.enum.case.md)
  The user doesn’t have enough storage space available to share the requested items.
- [NSCloudSharingTooManyParticipantsError](./nscloudsharingtoomanyparticipantserror-c.enum.case.md)
  Additional participants couldn’t be added to the share, because the limit was reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscloudsharingconflicterror-c.enum.case)*