# routeDataChannel

**Framework**: AVSystemRouting  
**Kind**: property  
**Role**: Instance Property

A data channel for communicating with the extension outside of any media session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readonly) AVSystemRouteDataChannel * routeDataChannel;
```

## Discussion

Use this channel for control messages, state synchronization, and other bidirectional communication needs that are not tied to a specific [`AVSystemRouteSession`](../avsystemroutesession-5i6j6.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-9kkj3/routedatachannel)*