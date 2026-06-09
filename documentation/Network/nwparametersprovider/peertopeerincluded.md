# peerToPeerIncluded(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Include peer-to-peer interfaces when connecting, listening, and browsing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func peerToPeerIncluded(_ included: Bool) -> Self
```

#### Discussion

> ❗ **Important**: Connections, Listeners, and Browsers using peer-to-peer interfaces can consume significantly more power and should not be kept running for longer than necessary. Peer-to-peer link technologies can be power-intensive. If a connection or listener with this flag enabled remains idle for an extended period, the system may return a `kDNSServiceErr_AWDLTimeout` error, transitioning it to a failed state that yields no further results. Any retry mechanism should implement exponential backoff or similar rate-limiting to avoid prolonged power drain.

This will not take effect if a specific interface is required. Applicable when advertising a Bonjour service on a listener, or connecting to a Bonjour service.

## Parameters

- `included`: True if peer-to-peer interfaces should be included, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/peertopeerincluded(_:))*