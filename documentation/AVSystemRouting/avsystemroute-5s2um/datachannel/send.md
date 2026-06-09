# send(_:)

**Framework**: AVSystemRouting  
**Kind**: method

Sends data to a remote application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func send(_ data: Data) async throws
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Discussion

Calling this function again before a previous send completes is safe; multiple send operations can be in-flight concurrently.

> **Note**: An error if the send operation fails.

## Parameters

- `data`: The data to send to the remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/datachannel/send(_:))*