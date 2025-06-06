# Background task cancellation

**Framework**: Foundation

Constants that indicate why a background task was canceled.

#### Overview

These values are used in conjunction with the [`NSURLErrorBackgroundTaskCancelledReasonKey`](nsurlerrorbackgroundtaskcancelledreasonkey.md) key in an [`NSError`](nserror.md) object’s `userInfo` dictionary.

## Topics

### Cancellation reasons
- [var NSURLErrorCancelledReasonBackgroundUpdatesDisabled: Int](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md)
  A reason that indicates the system canceled the background task because background tasks are disabled.
- [var NSURLErrorCancelledReasonInsufficientSystemResources: Int](nsurlerrorcancelledreasoninsufficientsystemresources.md)
  A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.
- [var NSURLErrorCancelledReasonUserForceQuitApplication: Int](nsurlerrorcancelledreasonuserforcequitapplication.md)
  A reason that indicates the system canceled the background task because the user force-quit the application.

## See Also

- [URL session error dictionary keys](url-session-error-dictionary-keys.md)
  Keys used in conjunction with error objects returned by URL sessions and tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/background-task-cancellation)*