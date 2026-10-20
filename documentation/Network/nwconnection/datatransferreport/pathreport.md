# NWConnection.DataTransferReport.PathReport

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A report that contains details about data transfer over a single network path.

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
struct PathReport
```

## Topics

### Identifying Paths
- [let interface: NWInterface](./pathreport/interface.md)
  The network interface this path used.
### Inspecting Application Metrics
- [let receivedApplicationByteCount: UInt64](./pathreport/receivedapplicationbytecount.md)
  The number of bytes the connection delivered.
- [let sentApplicationByteCount: UInt64](./pathreport/sentapplicationbytecount.md)
  The number of bytes sent on the connection.
### Inspecting Transport Metrics
- [let receivedTransportByteCount: UInt64](./pathreport/receivedtransportbytecount.md)
  The number of bytes the transport protocol delivered.
- [let receivedTransportDuplicateByteCount: UInt64](./pathreport/receivedtransportduplicatebytecount.md)
  The number of duplicated bytes the transport protocol detected.
- [let receivedTransportOutOfOrderByteCount: UInt64](./pathreport/receivedtransportoutoforderbytecount.md)
  The number of bytes the transport protocol received out of order.
- [let sentTransportByteCount: UInt64](./pathreport/senttransportbytecount.md)
  The number of bytes sent into the transport protocol.
- [let retransmittedTransportByteCount: UInt64](./pathreport/retransmittedtransportbytecount.md)
  The number of bytes the transport protocol retransmitted.
- [let transportSmoothedRTT: TimeInterval](./pathreport/transportsmoothedrtt.md)
  The smoothed round-trip time the transport protocol measured.
- [let transportMinimumRTT: TimeInterval](./pathreport/transportminimumrtt.md)
  The minimum round-trip time the transport protocol measured.
- [let transportRTTVariance: TimeInterval](./pathreport/transportrttvariance.md)
  The variance of the round-trip time the transport protocol measured.
### Inspecting Packet Metrics
- [let receivedIPPacketCount: UInt64](./pathreport/receivedippacketcount.md)
  The number of IP packets the connection received.
- [let sentIPPacketCount: UInt64](./pathreport/sentippacketcount.md)
  The number of IP packets the connection sent.
### Instance Properties
- [var radioType: NWInterface.RadioType?](./pathreport/radiotype.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Examining Data Transfer
- [let aggregatePathReport: NWConnection.DataTransferReport.PathReport](./aggregatepathreport.md)
  A report that sums counts across all network paths.
- [let pathReports: [NWConnection.DataTransferReport.PathReport]](./pathreports.md)
  An array of reports for each network path the connection used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport)*