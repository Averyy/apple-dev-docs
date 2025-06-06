# retransmittedTransportByteCount

**Framework**: Network  
**Kind**: property

The number of bytes the transport protocol retransmitted.

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
let retransmittedTransportByteCount: UInt64
```

## See Also

- [let receivedTransportByteCount: UInt64](nwconnection/datatransferreport/pathreport/receivedtransportbytecount.md)
  The number of bytes the transport protocol delivered.
- [let receivedTransportDuplicateByteCount: UInt64](nwconnection/datatransferreport/pathreport/receivedtransportduplicatebytecount.md)
  The number of duplicated bytes the transport protocol detected.
- [let receivedTransportOutOfOrderByteCount: UInt64](nwconnection/datatransferreport/pathreport/receivedtransportoutoforderbytecount.md)
  The number of bytes the transport protocol received out of order.
- [let sentTransportByteCount: UInt64](nwconnection/datatransferreport/pathreport/senttransportbytecount.md)
  The number of bytes sent into the transport protocol.
- [let transportSmoothedRTT: TimeInterval](nwconnection/datatransferreport/pathreport/transportsmoothedrtt.md)
  The smoothed round-trip time the transport protocol measured.
- [let transportMinimumRTT: TimeInterval](nwconnection/datatransferreport/pathreport/transportminimumrtt.md)
  The minimum round-trip time the transport protocol measured.
- [let transportRTTVariance: TimeInterval](nwconnection/datatransferreport/pathreport/transportrttvariance.md)
  The variance of the round-trip time the transport protocol measured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport/retransmittedtransportbytecount)*