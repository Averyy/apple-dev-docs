# URL Loading System error info keys

**Framework**: Foundation

Recognize these keys from the user info dictionary of error objects produced by URL Loading APIs.

#### Overview

These keys are only present in the [`NSURLErrorDomain`](nsurlerrordomain.md).

## Topics

### Keys
- [let NSURLErrorFailingURLErrorKey: String](nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLPeerTrustErrorKey: String](nsurlerrorfailingurlpeertrusterrorkey.md)
  The state of a failed SSL handshake.
- [let NSURLErrorFailingURLStringErrorKey: String](nsurlerrorfailingurlstringerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md)
  Reasons that indicate why the system canceled a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
### Deprecated
- [let NSErrorFailingURLStringKey: String](nserrorfailingurlstringkey.md)
  The URL that caused the error.

## See Also

- [struct URLError](urlerror.md)
  Error codes returned by URL loading APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url-loading-system-error-info-keys)*