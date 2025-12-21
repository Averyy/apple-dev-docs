# URLError.NetworkUnavailableReason.expensive

**Framework**: Foundation  
**Kind**: case

A reason that indicates network is unavailable because the system marked the interface as expensive.

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
case expensive
```

#### Discussion

The system determines what constitutes “expensive” based on the nature of the network interface and other factors. iOS 13 considers most cellular networks and personal hotspots expensive.

This reason occurs when the following conditions are true:

- The only available network interfaces are expensive.
- The [`URLSessionConfiguration`](urlsessionconfiguration.md) property [`allowsExpensiveNetworkAccess`](urlsessionconfiguration/allowsexpensivenetworkaccess.md) is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [URLError.NetworkUnavailableReason.cellular](urlerror/networkunavailablereason-swift.enum/cellular.md)
  A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.constrained](urlerror/networkunavailablereason-swift.enum/constrained.md)
  A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/expensive)*