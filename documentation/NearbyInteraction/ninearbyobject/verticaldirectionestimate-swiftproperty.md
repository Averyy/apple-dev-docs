# verticalDirectionEstimate

**Framework**: Nearby Interaction  
**Kind**: property

The estimation of a nearby object’s vertical position as it relates to the user’s device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

The framework sets a value of this property when [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) is `true`.

The framework periodically sets the value of this property when vertical positioning is available. Otherwise, the framework sets the value to [`NINearbyObject.VerticalDirectionEstimate.unknown`](ninearbyobject/verticaldirectionestimate-swift.enum/unknown.md).

## See Also

- [var direction: simd_float3?](ninearbyobject/direction-4qh5w.md)
  A vector that points from the user’s device in the direction of the peer device.
- [var horizontalAngle: Float?](ninearbyobject/horizontalangle-hsg.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/verticaldirectionestimate-swift.property)*