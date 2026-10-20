# NSURLErrorFailingURLStringErrorKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

The URL which caused a load to fail.

**Availability**:
- iOS 4.0+ - Deprecated in 18.4
- iPadOS 4.0+ - Deprecated in 18.4
- Mac Catalyst 13.1+ - Deprecated in 18.4
- macOS 10.6+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Use NSURLErrorFailingURLErrorKey instead

## Declaration

```swift
let NSURLErrorFailingURLStringErrorKey: String
```

```c
extern NSString * const NSURLErrorFailingURLStringErrorKey;
```

#### Discussion

The corresponding value is an [`NSString`](./nsstring.md) object.

This constant supersedes [`NSErrorFailingURLStringKey`](./nserrorfailingurlstringkey.md), which was deprecated starting in macOS 10.6.  Both constants refer to the same value for backward-compatibility, but this symbol name has a better prefix.

## See Also

### Keys
- [let NSURLErrorFailingURLErrorKey: String](./nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLPeerTrustErrorKey: String](./nsurlerrorfailingurlpeertrusterrorkey.md)
  The state of a failed SSL handshake.
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](./nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](./url-session-background-task-cancellation-reasons.md)
  Reasons that indicate why the system canceled a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](./nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](./urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorfailingurlstringerrorkey)*