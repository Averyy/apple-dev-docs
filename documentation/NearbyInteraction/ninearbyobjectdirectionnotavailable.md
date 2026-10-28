# NINearbyObjectDirectionNotAvailable

**Framework**: Nearby Interaction  
**Kind**: var  
**Role**: Global Variable

A value that indicates that a nearby object’s direction is unavailable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```c
extern simd_float3 NINearbyObjectDirectionNotAvailable;
```

## Mentions

- [Initiating and maintaining a session](./initiating-and-maintaining-a-session.md)

## Discussion

The framework sets [`direction`](./ninearbyobject/direction-5xcld.md) to the value of this property when it’s unable to acquire the nearby object’s direction at any given time.

To increase the direction availability, enable [`isCameraAssistanceEnabled`](./ninearbypeerconfiguration/iscameraassistanceenabled.md).

## See Also

### Acquiring relative direction
- [direction](./ninearbyobject/direction-5xcld.md)
  A vector that points from the user’s device in the direction of the peer device.
- [horizontalAngle](./ninearbyobject/horizontalangle-9ibky.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [NINearbyObjectAngleNotAvailable](./ninearbyobjectanglenotavailable.md)
  A value that indicates that a nearby object’s horizontal angle is unavailable.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](./ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.
- [NINearbyObject.VerticalDirectionEstimate](./ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobjectdirectionnotavailable)*