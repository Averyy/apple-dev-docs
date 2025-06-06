# horizontalAngle

**Framework**: Nearby Interaction  
**Kind**: property

An angle in radians that indicates the azimuthal direction to the nearby object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
var horizontalAngle: Float? { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

The framework sets a value of this property when [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) is `true`.

This property is `nil` when direction is unavailable, such as when the app runs on Apple Watch.

## See Also

- [var direction: simd_float3?](ninearbyobject/direction-4qh5w.md)
  A vector that points from the user’s device in the direction of the peer device.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.
- [NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/horizontalangle-hsg)*