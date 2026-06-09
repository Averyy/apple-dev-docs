# nw_tcp_set_max_pacing_rate(_:_:)

**Framework**: Network  
**Kind**: func

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
func nw_tcp_set_max_pacing_rate(_ metadata: nw_protocol_metadata_t, _ max_pacing_rate: UInt64) -> Int32
```

#### Return Value

Returns 0 on success, or an error code on failure.

#### Discussion

Set the maximum pacing rate for TCP transmission in bytes per second. TCP pacing spreads out packet transmission to avoid bursts and reduce network congestion. The actual pacing rate used will be the minimum of this value and the rate computed from cwnd/RTT.

```None
A value of 0 or UINT64_MAX means unlimited (disables pacing).
```

## Parameters

- `metadata`: A TCP protocol metadata object from an established connection.
- `max_pacing_rate`: Maximum pacing rate in bytes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_tcp_set_max_pacing_rate(_:_:))*