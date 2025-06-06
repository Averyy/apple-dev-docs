# receiveTime

**Framework**: Network  
**Kind**: property

The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.

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
var receiveTime: UInt64 { get }
```

## See Also

- [var shouldCalculateReceiveTime: Bool](nwprotocolip/options/shouldcalculatereceivetime.md)
  A Boolean that indicates whether a connection delivers receive timestamps for IP packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/metadata/receivetime)*