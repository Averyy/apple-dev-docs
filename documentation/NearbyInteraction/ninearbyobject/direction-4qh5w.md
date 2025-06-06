# direction

**Framework**: Nearby Interaction  
**Kind**: property

A vector that points from the user’s device in the direction of the peer device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.4+
- watchOS 7.3+

## Declaration

```swift
var direction: simd_float3? { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

This property is `nil` when direction is unavailable, such as when the app runs on Apple Watch.

On iPhone, it’s possible to recieve direction for nearby third-party accessories in sessions that enable [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md).

##### Interpret Direction

This property is a Cartesian triplet (x,y,z) in normalized units with a range of `[0..1]`. Nearby Interaction models [`direction`](ninearbyobject/direction-4qh5w.md) as a coordinate on a sphere, such that a ray cast from the sphere’s center through the coordinate points toward the peer device. For each axis, the sphere center is at coordinate 0, and the surface is at coordinate 1. As the user looks at the device’s screen,

- The x-axis extends positively to the right.
- The y-axis extends positively upward.
- The z-axis extends negatively from the device’s center, away from the user.

The following figure illustrates the direction-vector coordinate space from two different angles.

![A diagram of a phone in two different orientations, each with a coordinate system that renders from an origin in the middle of the device. The phone on the left shows the back of the phone, with an up-axis labeled “+y”. Its horizontal axis points left, and is labeled “+x”. Its z-axis points toward the reader, and is labeled “-z”. The phone on the right faces toward the reader, with an up-axis labeled “+y”. Its horizontal axis points right and is labeled “+x”. Its z-axis points away from the reader, and is labeled “-z”.](https://docs-assets.developer.apple.com/published/eaa9b90498bacaef6df0517071bb32d9/media-3798530%402x.png)

For more information, see [`Initiating and maintaining a session`](initiating-and-maintaining-a-session.md).

## See Also

- [var horizontalAngle: Float?](ninearbyobject/horizontalangle-hsg.md)
  An angle in radians that indicates the azimuthal direction to the nearby object.
- [var verticalDirectionEstimate: NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.property.md)
  The estimation of a nearby object’s vertical position as it relates to the user’s device.
- [NINearbyObject.VerticalDirectionEstimate](ninearbyobject/verticaldirectionestimate-swift.enum.md)
  Estimations of a nearby object’s vertical position in relation to the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject/direction-4qh5w)*