# URLError.NetworkUnavailableReason

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.

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
enum NetworkUnavailableReason
```

#### Overview

The network may be unavailable due to restrictions placed on the [`URLSessionConfiguration`](../urlsessionconfiguration.md), such as [`allowsConstrainedNetworkAccess`](../urlsessionconfiguration/allowsconstrainednetworkaccess.md), [`allowsExpensiveNetworkAccess`](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) and [`allowsCellularAccess`](../urlsessionconfiguration/allowscellularaccess.md).

## Topics

### Unavailability reasons
- [URLError.NetworkUnavailableReason.cellular](./networkunavailablereason-swift.enum/cellular.md)
  A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.constrained](./networkunavailablereason-swift.enum/constrained.md)
  A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
- [URLError.NetworkUnavailableReason.expensive](./networkunavailablereason-swift.enum/expensive.md)
  A reason that indicates network is unavailable because the system marked the interface as expensive.
### Enumeration Cases
- [URLError.NetworkUnavailableReason.ultraConstrained](./networkunavailablereason-swift.enum/ultraconstrained.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](./networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum)*