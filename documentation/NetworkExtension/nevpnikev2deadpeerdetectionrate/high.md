# NEVPNIKEv2DeadPeerDetectionRate.high

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

Run dead peer detection once every 1 minute. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case high
```

```c
NEVPNIKEv2DeadPeerDetectionRateHigh
```

## See Also

### Detection rates
- [NEVPNIKEv2DeadPeerDetectionRate.none](./none.md)
  Do not perform dead peer detection.
- [NEVPNIKEv2DeadPeerDetectionRate.low](./low.md)
  Run dead peer detection once every 30 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
- [NEVPNIKEv2DeadPeerDetectionRate.medium](./medium.md)
  Run dead peer detection once every 10 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/high)*