# NINearbyObject.VerticalDirectionEstimate

**Framework**: Nearby Interaction  
**Kind**: enum

Estimations of a nearby object’s vertical position in relation to the user’s device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
enum VerticalDirectionEstimate
```

#### Overview

The framework sets a nearby object’s [`verticalDirectionEstimate`](ninearbyobject/verticaldirectionestimate-swift.property.md) to an option of this enumeration when [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) is `true`.

## Topics

### Relative vertical location
- [NINearbyObject.VerticalDirectionEstimate.unknown](ninearbyobject/verticaldirectionestimate-swift.enum/unknown.md)
  An indication that the nearby object resides at an unknown vertical location.
- [NINearbyObject.VerticalDirectionEstimate.same](ninearbyobject/verticaldirectionestimate-swift.enum/same.md)
  An indication that the nearby object resides at an equivalent vertical location as the user’s device.
- [NINearbyObject.VerticalDirectionEstimate.above](ninearbyobject/verticaldirectionestimate-swift.enum/above.md)
  An indication that the nearby object resides at a higher vertical location than the user’s device.
- [NINearbyObject.VerticalDirectionEstimate.below](ninearbyobject/verticaldirectionestimate-swift.enum/below.md)
  An indication that the nearby object resides at a lower vertical location than the user’s device.
- [NINearbyObject.VerticalDirectionEstimate.aboveOrBelow](ninearbyobject/verticaldirectionestimate-swift.enum/aboveorbelow.md)
  An indication that the nearby object doesn’t reside at the same vertical location as the user’s device.
### Initializers
- [init?(rawValue: Int)](ninearbyobject/verticaldirectionestimate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var direction: simd_float3?](ninearbyobject/direction-4qh5w.md)
  A vector that points from the user’s device in the direction of the peer device.
- [var horizontalAngle: Float?](ninearbyobject/horizontalangle-hsg.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/verticaldirectionestimate-swift.enum)*