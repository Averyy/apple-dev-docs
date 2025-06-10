# allowsConstrainedNetworkAccess

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.

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
var allowsConstrainedNetworkAccess: Bool { get set }
```

#### Discussion

In iOS 13 and later, users can set their device to use Low Data Mode as one of the Cellular Data Options in the Settings app. Users can turn on Low Data Mode to reduce your app’s network data usage. This property controls a URL session’s behavior when the user turns on Low Data Mode. If there are no nonconstrained network interfaces available and the session’s [`allowsConstrainedNetworkAccess`](urlsessionconfiguration/allowsconstrainednetworkaccess.md) property is [`false`](https://developer.apple.com/documentation/swift/false), any task created from the session fails. In this case, the error provided when the task fails has a [`networkUnavailableReason`](urlerror/networkunavailablereason-swift.property.md) property whose value is [`NSURLErrorNetworkUnavailableReasonConstrained`](nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained.md).

Limit your app’s of use of constrained network access to user-initiated tasks, and put off discretionary tasks until a nonconstrained interface becomes available. To do this, set [`allowsConstrainedNetworkAccess`](urlsessionconfiguration/allowsconstrainednetworkaccess.md) (and [`allowsExpensiveNetworkAccess`](urlsessionconfiguration/allowsexpensivenetworkaccess.md)) to [`false`](https://developer.apple.com/documentation/swift/false) and [`waitsForConnectivity`](urlsessionconfiguration/waitsforconnectivity.md) to [`true`](https://developer.apple.com/documentation/swift/true). This way, your [`URLSessionTask`](urlsessiontask.md) waits for a suitable interface to become available before sending or receiving data.

## See Also

- [var allowsExpensiveNetworkAccess: Bool](urlsessionconfiguration/allowsexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/allowsconstrainednetworkaccess)*