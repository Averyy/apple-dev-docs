# URLError.NetworkUnavailableReason.cellular

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.

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
case cellular
```

#### Discussion

This reason occurs when cellular is the only available network interface, but the [`URLSessionConfiguration`](../../urlsessionconfiguration.md) property [`allowsCellularAccess`](../../urlsessionconfiguration/allowscellularaccess.md) is [`false`](../../../Swift/false.md).

## See Also

### Unavailability reasons
- [URLError.NetworkUnavailableReason.constrained](./constrained.md)
  A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
- [URLError.NetworkUnavailableReason.expensive](./expensive.md)
  A reason that indicates network is unavailable because the system marked the interface as expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/networkunavailablereason-swift.enum/cellular)*