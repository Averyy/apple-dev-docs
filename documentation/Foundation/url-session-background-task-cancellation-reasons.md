# URL Session Background Task Cancellation Reasons

**Framework**: Foundation

Reasons that indicate why the system canceled a background task.

## Topics

### Cancellation reasons
- [var NSURLErrorCancelledReasonBackgroundUpdatesDisabled: Int](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md)
  A reason that indicates the system canceled the background task because background tasks are disabled.
- [var NSURLErrorCancelledReasonInsufficientSystemResources: Int](nsurlerrorcancelledreasoninsufficientsystemresources.md)
  A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.
- [var NSURLErrorCancelledReasonUserForceQuitApplication: Int](nsurlerrorcancelledreasonuserforcequitapplication.md)
  A reason that indicates the system canceled the background task because the user force-quit the application.

## See Also

- [let NSURLErrorFailingURLErrorKey: String](nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLPeerTrustErrorKey: String](nsurlerrorfailingurlpeertrusterrorkey.md)
  The state of a failed SSL handshake.
- [let NSURLErrorFailingURLStringErrorKey: String](nsurlerrorfailingurlstringerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url-session-background-task-cancellation-reasons)*