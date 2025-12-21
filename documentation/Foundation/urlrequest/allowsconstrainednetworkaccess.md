# allowsConstrainedNetworkAccess

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the request may use the network when the user has specified Low Data Mode.

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
var allowsConstrainedNetworkAccess: Bool { get set }
```

#### Discussion

In iOS 13 and later, users can set their device to use Low Data Mode as one of the Cellular Data Options in the Settings app. Users can turn on Low Data Mode to reduce your app’s network data usage. This property controls the request’s behavior when the user turns on Low Data Mode. If there are no nonconstrained network interfaces available and the request’s [`allowsConstrainedNetworkAccess`](urlrequest/allowsconstrainednetworkaccess.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), any connection created from the request fails. In this case, the error provided when the connection fails has a [`networkUnavailableReason`](urlerror/networkunavailablereason-swift.property.md) property whose value is [`NSURLErrorNetworkUnavailableReasonConstrained`](nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained.md).

Setting this property on a request overrides the [`allowsConstrainedNetworkAccess`](urlsessionconfiguration/allowsconstrainednetworkaccess.md) property of [`URLSessionConfiguration`](urlsessionconfiguration.md). For example, if the session configuration’s [`allowsConstrainedNetworkAccess`](urlsessionconfiguration/allowsconstrainednetworkaccess.md) value is [`false`](https://developer.apple.com/documentation/Swift/false), and you create a task from a request whose [`allowsConstrainedNetworkAccess`](urlrequest/allowsconstrainednetworkaccess.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the task treats the value as [`true`](https://developer.apple.com/documentation/Swift/true).

Limit your app’s of use of constrained network access to user-initiated tasks, and put off discretionary tasks until a nonconstrained interface becomes available.

## See Also

- [var allowsExpensiveNetworkAccess: Bool](urlrequest/allowsexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/allowsconstrainednetworkaccess)*