# dataChannel

**Framework**: AVSystemRouting  
**Kind**: property

The data channel for sending and receiving data with the remote app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var dataChannel: AVSystemRoute.DataChannel? { get }
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Discussion

This property is always non-nil when obtained from a successful call to [`start()`](avsystemroutesession-gp78/start().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-98ioq/datachannel)*