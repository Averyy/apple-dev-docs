# NSURLErrorFailingURLPeerTrustErrorKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

The state of a failed SSL handshake.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSURLErrorFailingURLPeerTrustErrorKey: String
```

```c
extern NSString * const NSURLErrorFailingURLPeerTrustErrorKey;
```

#### Discussion

The corresponding value is the [`SecTrust`](../Security/sectrust.md) object.

## See Also

### Keys
- [let NSURLErrorFailingURLErrorKey: String](./nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLStringErrorKey: String](./nsurlerrorfailingurlstringerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](./nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](./url-session-background-task-cancellation-reasons.md)
  Reasons that indicate why the system canceled a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](./nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](./urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
- [NSURLErrorNetworkUnavailableReason](./nsurlerrornetworkunavailablereason.md)
  An enumeration of reasons why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorfailingurlpeertrusterrorkey)*