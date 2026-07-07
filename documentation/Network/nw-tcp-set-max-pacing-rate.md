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

Returns 0 on success, or a POSIX errno value on failure (e.g. EINVAL if metadata is not a TCP metadata object, or the underlying socket error).

#### Discussion

Set a maximum pacing rate for a TCP connection, in bytes per second.

TCP pacing spreads outgoing packet transmission across time to avoid bursts and reduce queueing in the network. With a cap in place, the on-wire rate is the minimum of (a) this cap, and (b) the rate computed from the congestion window divided by smoothed RTT. The cap therefore never raises throughput above what congestion control would otherwise allow.

```None
A value of 0 or UINT64_MAX disables pacing on this connection — the
connection sends without pacing (subject only to congestion control).

Rates in the open interval (0, 12500) are silently clamped up to
12500 bytes/second (100 Kbps). Callers needing genuinely sub-100-Kbps
pacing must shape at the application layer.

The cap may be updated at any time during the lifetime of an
established connection. Each call replaces the prior value.
```

## Parameters

- `metadata`: A TCP protocol metadata object from an established connection (e.g. obtained via nw_connection_access_established_protocol_metadata).
- `max_pacing_rate`: Maximum pacing rate in bytes per second. 0 or UINT64_MAX disables pacing on this connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_tcp_set_max_pacing_rate(_:_:))*