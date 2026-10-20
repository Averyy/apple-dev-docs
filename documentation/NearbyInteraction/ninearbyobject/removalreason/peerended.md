# NINearbyObject.RemovalReason.peerEnded

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

The peer ended the session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
case peerEnded
```

```c
NINearbyObjectRemovalReasonPeerEnded
```

#### Discussion

The framework provides this removal reason when the peer app calls [`invalidate()`](../../nisession/invalidate%28%29.md).

## See Also

### Reasons
- [NINearbyObject.RemovalReason.timeout](./timeout.md)
  NI timed out the session.
- [NINearbyObject.RemovalReason.timeout](./timeout.md)
  NI timed out the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/removalreason/peerended)*