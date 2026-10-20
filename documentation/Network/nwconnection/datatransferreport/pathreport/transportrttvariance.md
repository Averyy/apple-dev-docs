# transportRTTVariance

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The variance of the round-trip time the transport protocol measured.

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
let transportRTTVariance: TimeInterval
```

## See Also

### Inspecting Transport Metrics
- [let receivedTransportByteCount: UInt64](./receivedtransportbytecount.md)
  The number of bytes the transport protocol delivered.
- [let receivedTransportDuplicateByteCount: UInt64](./receivedtransportduplicatebytecount.md)
  The number of duplicated bytes the transport protocol detected.
- [let receivedTransportOutOfOrderByteCount: UInt64](./receivedtransportoutoforderbytecount.md)
  The number of bytes the transport protocol received out of order.
- [let sentTransportByteCount: UInt64](./senttransportbytecount.md)
  The number of bytes sent into the transport protocol.
- [let retransmittedTransportByteCount: UInt64](./retransmittedtransportbytecount.md)
  The number of bytes the transport protocol retransmitted.
- [let transportSmoothedRTT: TimeInterval](./transportsmoothedrtt.md)
  The smoothed round-trip time the transport protocol measured.
- [let transportMinimumRTT: TimeInterval](./transportminimumrtt.md)
  The minimum round-trip time the transport protocol measured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport/transportrttvariance)*