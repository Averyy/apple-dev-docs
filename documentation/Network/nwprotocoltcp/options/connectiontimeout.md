# connectionTimeout

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The number of seconds that TCP waits before timing out its handshake.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var connectionTimeout: Int { get set }
```

## See Also

### Setting Timeouts
- [var connectionDropTime: Int](./connectiondroptime.md)
  The timeout, in seconds, for TCP retransmission attempts.
- [var persistTimeout: Int](./persisttimeout.md)
  The TCP persist timeout, in seconds, as defined by RFC 6429.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/connectiontimeout)*