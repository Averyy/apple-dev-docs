# NSURLErrorNetworkUnavailableReasonKey

**Framework**: Foundation  
**Kind**: var

The reason the network was unavailable for a task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let NSURLErrorNetworkUnavailableReasonKey: String
```

#### Discussion

The value associated with this key is an [`NSNumber`](nsnumber.md). For possible values, see [`NSURLErrorNetworkUnavailableReason`](nsurlerrornetworkunavailablereason.md).

## See Also

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
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereasonkey)*