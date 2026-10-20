# networkUnavailableReason

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The reason the network was unavailable for a task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var networkUnavailableReason: URLError.NetworkUnavailableReason? { get }
```

#### Discussion

The network may be unavailable due to restrictions placed on the [`URLSessionConfiguration`](../urlsessionconfiguration.md), such as [`allowsConstrainedNetworkAccess`](../urlsessionconfiguration/allowsconstrainednetworkaccess.md), [`allowsExpensiveNetworkAccess`](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) and [`allowsCellularAccess`](../urlsessionconfiguration/allowscellularaccess.md).

If the error doesn’t involve network unavailability, this property is `nil`.

## See Also

### Error details
- [var failingURL: URL?](./failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](./failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var failureURLString: String?](./failureurlstring.md)
  The string for the URL which caused a load to fail.
- [var downloadTaskResumeData: Data?](./downloadtaskresumedata.md)
  An opaque data object used to resume a failed download task.
- [var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason?](./backgroundtaskcancelledreason-swift.property.md)
  The reason for canceling a background task.
- [URLError.BackgroundTaskCancelledReason](./backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [URLError.NetworkUnavailableReason](./networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.property)*