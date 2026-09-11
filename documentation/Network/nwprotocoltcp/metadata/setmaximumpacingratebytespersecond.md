# setMaximumPacingRateBytesPerSecond(_:)

**Framework**: Network  
**Kind**: method

Set the maximum pacing rate for this TCP connection, in bytes per second.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func setMaximumPacingRateBytesPerSecond(_ maximumPacingRateBytesPerSecond: UInt64?)
```

#### Discussion

TCP pacing spreads out packet transmission to avoid bursts and reduce network congestion. The actual on-wire rate is the minimum of this cap and the rate computed from the congestion window and RTT, so this value never increases throughput above what congestion control allows.

Pass `nil` to disable pacing on this connection — the connection will send without pacing (subject only to congestion control).

## Parameters

- `maximumPacingRateBytesPerSecond`:  Maximum pacing rate in bytes per second, or `nil` to disable pacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/metadata/setmaximumpacingratebytespersecond(_:))*