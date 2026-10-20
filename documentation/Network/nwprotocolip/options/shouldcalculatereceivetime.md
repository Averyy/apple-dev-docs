# shouldCalculateReceiveTime

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a connection delivers receive timestamps for IP packets.

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
var shouldCalculateReceiveTime: Bool { get set }
```

## See Also

### Related Documentation
- [var receiveTime: UInt64](../metadata/receivetime.md)
  The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.
### Customizing IP Behavior
- [var hopLimit: UInt8](./hoplimit.md)
  The default hop limit for packets a connection generates.
- [var useMinimumMTU: Bool](./useminimummtu.md)
  A Boolean indicating that the connection uses the  minimum MTU value, which is 1280 bytes for IPv6.
- [var disableFragmentation: Bool](./disablefragmentation.md)
  A Boolean that indicates whether fragmentation is disabled on outbound packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/options/shouldcalculatereceivetime)*