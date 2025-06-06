# NINearbyObject

**Framework**: Nearby Interaction  
**Kind**: class

Location information for a peer device in an interaction session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class NINearbyObject
```

#### Overview

A nearby object refers to a peer Apple device or third-party accessory.

When the framework is ready to provide your app with information about a nearby object’s relative position, it calls your delegate’s [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md) implementation.

If a session can’t provide peer direction or distance, it sets the values to `nil`. In Objective-C, the session uses the [`NINearbyObjectDirectionNotAvailable`](ninearbyobjectdirectionnotavailable.md) and [`NINearbyObjectDistanceNotAvailable`](ninearbyobjectdistancenotavailable.md) values to indicate missing direction or distance.

For more information, see [`Initiating and maintaining a session`](initiating-and-maintaining-a-session.md).

## Topics

### Identifying a nearby device
- [var discoveryToken: NIDiscoveryToken](ninearbyobject/discoverytoken.md)
  A unique identifier for a peer device in the session.
### Acquring relative distance
- [var distance: Float?](ninearbyobject/distance-676dm.md)
  The distance from the user’s device to the peer device in meters.
### Acquiring relative direction
- [var direction: simd_float3?](ninearbyobject/direction-4qh5w.md)
  A vector that points from the user’s device in the direction of the peer device.
- [var horizontalAngle: Float?](ninearbyobject/horizontalangle-hsg.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.
- [NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.
### Explaining participation
- [NINearbyObject.RemovalReason](ninearbyobject/removalreason.md)
  The reason a session removed a nearby object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol NISessionDelegate](nisessiondelegate.md)
  An object that monitors and reacts to session updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject)*