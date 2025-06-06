# shouldCalculateReceiveTime

**Framework**: Network  
**Kind**: property

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

- [var receiveTime: UInt64](nwprotocolip/metadata/receivetime.md)
  The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.
- [var hopLimit: UInt8](nwprotocolip/options/hoplimit.md)
  The default hop limit for packets a connection generates.
- [var useMinimumMTU: Bool](nwprotocolip/options/useminimummtu.md)
  A Boolean indicating that the connection uses the  minimum MTU value, which is 1280 bytes for IPv6.
- [var disableFragmentation: Bool](nwprotocolip/options/disablefragmentation.md)
  A Boolean that indicates whether fragmentation is disabled on outbound packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/options/shouldcalculatereceivetime)*