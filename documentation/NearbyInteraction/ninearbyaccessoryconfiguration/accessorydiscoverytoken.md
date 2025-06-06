# accessoryDiscoveryToken

**Framework**: Nearby Interaction  
**Kind**: property

An identifier for the accessory in a session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var accessoryDiscoveryToken: NIDiscoveryToken { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

The value of this property refers to a specific peer accessory. To match [`distance`](ninearbyobject/distance-676dm.md) updates your app receives through a session with a peer using [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md), compare the argument object’s discovery token with the value of this property.

Subsequent sessions with the same peer device produce a different value for this property. For user privacy, the system assigns a random number unique to the session that prevents the correlation of this property with a particular device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration/accessorydiscoverytoken)*