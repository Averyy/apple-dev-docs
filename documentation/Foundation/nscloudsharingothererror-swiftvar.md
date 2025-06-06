# NSCloudSharingOtherError

**Framework**: Foundation  
**Kind**: var

An otherwise unspecified cloud-sharing error occurred.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var NSCloudSharingOtherError: Int { get }
```

#### Discussion

For CloudKit sharing, use the [`NSUnderlyingErrorKey`](nsunderlyingerrorkey.md), whose value is a [`CKErrorDomain`](https://developer.apple.com/documentation/CloudKit/CKErrorDomain) error, to discover the specific error. Refer to the [`CloudKit`](https://developer.apple.com/documentation/CloudKit) documentation for the proper response to these errors.

## See Also

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
- [var NSCloudSharingQuotaExceededError: Int](nscloudsharingquotaexceedederror-swift.var.md)
  The user doesn’t have enough storage space available to share the requested items.
- [var NSCloudSharingTooManyParticipantsError: Int](nscloudsharingtoomanyparticipantserror-swift.var.md)
  Additional participants couldn’t be added to the share, because the limit was reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscloudsharingothererror-swift.var)*