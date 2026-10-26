# NINearbyObjectAngleNotAvailable

**Framework**: Nearby Interaction  
**Kind**: var  
**Role**: Global Variable

A value that indicates that a nearby object’s horizontal angle is unavailable.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```c
extern float NINearbyObjectAngleNotAvailable;
```

#### Discussion

The framework sets [`horizontalAngle`](./ninearbyobject/horizontalangle-9ibky.md) to the value of this property when it’s unable to acquire the nearby object’s horizontal angle at any given time.

## See Also

### Acquiring relative direction
- [direction](./ninearbyobject/direction-5xcld.md)
  A vector that points from the user’s device in the direction of the peer device.
- [NINearbyObjectDirectionNotAvailable](./ninearbyobjectdirectionnotavailable.md)
  A value that indicates that a nearby object’s direction is unavailable.
- [horizontalAngle](./ninearbyobject/horizontalangle-9ibky.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](./ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.
- [NINearbyObject.VerticalDirectionEstimate](./ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobjectanglenotavailable)*