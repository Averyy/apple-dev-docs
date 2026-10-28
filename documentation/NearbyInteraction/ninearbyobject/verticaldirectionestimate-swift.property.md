# verticalDirectionEstimate

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NINearbyObjectVerticalDirectionEstimate verticalDirectionEstimate;
```

## Mentions

- [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md)

## Discussion

The framework sets a value of this property when [`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md) is `true`.

The framework periodically sets the value of this property when vertical positioning is available. Otherwise, the framework sets the value to [`NINearbyObject.VerticalDirectionEstimate.unknown`](./verticaldirectionestimate-swift.enum/unknown.md).

## See Also

### Acquiring relative direction
- [var direction: simd_float3?](./direction-4qh5w.md)
  A vector that points from the user’s device in the direction of the peer device.
- [var horizontalAngle: Float?](./horizontalangle-hsg.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [NINearbyObject.VerticalDirectionEstimate](./verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.
- [direction](./direction-5xcld.md)
  A vector that points from the user’s device in the direction of the peer device.
- [NINearbyObjectDirectionNotAvailable](../ninearbyobjectdirectionnotavailable.md)
  A value that indicates that a nearby object’s direction is unavailable.
- [horizontalAngle](./horizontalangle-9ibky.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [NINearbyObjectAngleNotAvailable](../ninearbyobjectanglenotavailable.md)
  A value that indicates that a nearby object’s horizontal angle is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/verticaldirectionestimate-swift.property)*