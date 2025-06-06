# NEVPNIKEv2DeadPeerDetectionRate.none

**Framework**: Network Extension  
**Kind**: case

Do not perform dead peer detection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

## See Also

- [NEVPNIKEv2DeadPeerDetectionRate.low](nevpnikev2deadpeerdetectionrate/low.md)
  Run dead peer detection once every 30 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
- [NEVPNIKEv2DeadPeerDetectionRate.medium](nevpnikev2deadpeerdetectionrate/medium.md)
  Run dead peer detection once every 10 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
- [NEVPNIKEv2DeadPeerDetectionRate.high](nevpnikev2deadpeerdetectionrate/high.md)
  Run dead peer detection once every 1 minute. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/none)*