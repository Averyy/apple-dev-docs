# routeDataChannel

**Framework**: AVSystemRouting  
**Kind**: property

A data channel for communicating with the extension outside of any media session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var routeDataChannel: AVSystemRoute.DataChannel { get }
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Discussion

Use this channel for control messages, state synchronization, and other bidirectional communication needs that are not tied to a specific [`AVSystemRouteSession`](avsystemroutesession-gp78.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/routedatachannel)*