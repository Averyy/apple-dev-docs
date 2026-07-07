# setMaximumPacingRateBytesPerSecond(_:)

**Framework**: Network  
**Kind**: method

Set the maximum pacing rate for this TCP connection, in bytes per second.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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