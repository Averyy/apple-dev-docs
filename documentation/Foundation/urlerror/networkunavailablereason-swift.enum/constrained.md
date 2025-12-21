# URLError.NetworkUnavailableReason.constrained

**Framework**: Foundation  
**Kind**: case

A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.

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
case constrained
```

#### Discussion

This reason occurs when the following conditions are true:

- The only available network is cellular.
- The user has enabled “Low Data Mode” option in the Cellular Data Options section of the Settings app.
- The [`URLSessionConfiguration`](urlsessionconfiguration.md) property [`allowsConstrainedNetworkAccess`](urlsessionconfiguration/allowsconstrainednetworkaccess.md) is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [URLError.NetworkUnavailableReason.cellular](urlerror/networkunavailablereason-swift.enum/cellular.md)
  A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [URLError.NetworkUnavailableReason.expensive](urlerror/networkunavailablereason-swift.enum/expensive.md)
  A reason that indicates network is unavailable because the system marked the interface as expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/constrained)*