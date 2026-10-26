# NSURLErrorNetworkUnavailableReason

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An enumeration of reasons why a task couldn’t satisfy networking constraints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
enum NSURLErrorNetworkUnavailableReason : NSInteger;
```

#### Overview

The network may be unavailable due to restrictions placed on the [`URLSessionConfiguration`](./urlsessionconfiguration.md), such as [`allowsConstrainedNetworkAccess`](./urlsessionconfiguration/allowsconstrainednetworkaccess.md), [`allowsExpensiveNetworkAccess`](./urlsessionconfiguration/allowsexpensivenetworkaccess.md) and [`allowsCellularAccess`](./urlsessionconfiguration/allowscellularaccess.md).

## Topics

### Unavailability reasons
- [NSURLErrorNetworkUnavailableReasonCellular](./nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasoncellular.md)
  A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [NSURLErrorNetworkUnavailableReasonConstrained](./nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained.md)
  A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
- [NSURLErrorNetworkUnavailableReasonExpensive](./nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonexpensive.md)
  A reason that indicates network is unavailable because the system marked the interface as expensive.
### Enumeration Cases
- [NSURLErrorNetworkUnavailableReasonUltraConstrained](./nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonultraconstrained.md)
  The network is unavailable because the ultra-constrained interface is not available.

## See Also

### Keys
- [let NSURLErrorFailingURLErrorKey: String](./nsurlerrorfailingurlerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorFailingURLPeerTrustErrorKey: String](./nsurlerrorfailingurlpeertrusterrorkey.md)
  The state of a failed SSL handshake.
- [let NSURLErrorFailingURLStringErrorKey: String](./nsurlerrorfailingurlstringerrorkey.md)
  The URL which caused a load to fail.
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](./nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](./url-session-background-task-cancellation-reasons.md)
  Reasons that indicate why the system canceled a background task.
- [let NSURLErrorNetworkUnavailableReasonKey: String](./nsurlerrornetworkunavailablereasonkey.md)
  The reason the network was unavailable for a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereason)*