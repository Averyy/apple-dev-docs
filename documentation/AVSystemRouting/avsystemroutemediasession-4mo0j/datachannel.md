# dataChannel

**Framework**: AVSystemRouting  
**Kind**: property  
**Role**: Instance Property

The data channel for sending and receiving data with the remote application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (readonly, nullable) AVSystemRouteDataChannel * dataChannel;
```

#### Discussion

This property is always non-nil when obtained from a successful call to [`start()`](../avsystemroutesession-gp78/start%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-4mo0j/datachannel)*