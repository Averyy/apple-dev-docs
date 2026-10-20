# allowsExpensiveNetworkAccess

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether connections may use a network interface that the system considers expensive.

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
var allowsExpensiveNetworkAccess: Bool { get set }
```

#### Discussion

The system determines what constitutes “expensive” based on the nature of the network interface and other factors. iOS 13 considers most cellular networks and personal hotspots expensive. If there are no nonexpensive network interfaces available and the request’s [`allowsExpensiveNetworkAccess`](./allowsexpensivenetworkaccess.md) property is [`false`](../../Swift/false.md), any task created from the request fails. In this case, the error provided when the task fails has a [`networkUnavailableReason`](../urlerror/networkunavailablereason-swift.property.md) property whose value is [`NSURLErrorNetworkUnavailableReasonExpensive`](../nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonexpensive.md).

Setting this property on a request overrides the [`allowsExpensiveNetworkAccess`](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) property of [`URLSessionConfiguration`](../urlsessionconfiguration.md). For example, if the session configuration’s [`allowsExpensiveNetworkAccess`](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) value is [`false`](../../Swift/false.md), and you create a task from a request whose [`allowsExpensiveNetworkAccess`](./allowsexpensivenetworkaccess.md) is [`true`](../../Swift/true.md), the task treats the value as [`true`](../../Swift/true.md).

Limit your app’s of use of expensive network access to user-initiated tasks, and put off discretionary tasks until a nonexpensive interface becomes available.

## See Also

### Supporting limited modes
- [var allowsConstrainedNetworkAccess: Bool](./allowsconstrainednetworkaccess.md)
  A Boolean value that indicates whether the request may use the network when the user has specified Low Data Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/allowsexpensivenetworkaccess)*