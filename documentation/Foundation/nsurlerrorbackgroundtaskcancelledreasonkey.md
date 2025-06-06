# NSURLErrorBackgroundTaskCancelledReasonKey

**Framework**: Foundation  
**Kind**: var

A key in the error dictionary that provides the reason for canceling a background task.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSURLErrorBackgroundTaskCancelledReasonKey: String
```

#### Discussion

The value associated with this key is an [`NSNumber`](nsnumber.md). For a list of possible values, see URL Session Background Task Cancellation Reasons.

## See Also

- [let NSURLErrorFailingURLErrorKey: String](nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLPeerTrustErrorKey: String](nsurlerrorfailingurlpeertrusterrorkey.md)
  The state of a failed SSL handshake.
- [let NSURLErrorFailingURLStringErrorKey: String](nsurlerrorfailingurlstringerrorkey.md)
  The URL which caused a load to fail.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md)
  Reasons that indicate why the system canceled a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey)*