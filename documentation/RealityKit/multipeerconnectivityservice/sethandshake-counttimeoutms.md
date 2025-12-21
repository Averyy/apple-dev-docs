# setHandshake(count:timeoutMs:)

**Framework**: RealityKit  
**Kind**: method

Configures handshake and timeout settings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func setHandshake(count: UInt32, timeoutMs: UInt32)
```

#### Discussion

When RealityKit begins syncing with a connected device, it sends that device a special message, called a , over the network and waits for a response. Once it receives the correct response, it begins syncing the local RealityKit scene with the other connected app.

By default, RealityKit sends at most two handshake packets to a peer and waits up to 25,000 ms (25 seconds) for the peer to respond before giving up and disconnecting. Call this method to change the timeout or the number of handshake packets to send.

## Parameters

- `count`: The maximum number of handshake packets to send to peers.
- `timeoutMs`: The maximum amount of time to wait for peers to respond to   handshake packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/multipeerconnectivityservice/sethandshake(count:timeoutms:))*