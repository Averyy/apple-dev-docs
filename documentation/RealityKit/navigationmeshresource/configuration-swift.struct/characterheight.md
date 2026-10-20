# characterHeight

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The height of characters using this Navigation Mesh, representing the minimum height of obstacles above a surface to allow it to be walkable, in meters.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var characterHeight: Double
```

## See Also

### Configuring agent movement
- [var characterRadius: Double](./characterradius.md)
  The radius of characters using this Navigation Mesh, representing the minimum distance from edges or obstacles that can still be walkable, in meters.
- [var walkableSlopeAngle: Double](./walkableslopeangle.md)
  The maximum slope angle that will allow a surface to be walkable, in degrees.
- [var walkableClimb: Double](./walkableclimb.md)
  The maximum height difference between two surfaces that a character can walk through, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/characterheight)*