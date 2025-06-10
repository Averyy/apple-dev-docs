# *(_:_:)

**Framework**: Spatial  
**Kind**: op

Calculates the spherical linear interpolation between the identity rotation and the RHS rotation at the LHS interpolation parameter.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func * (lhs: Float, rhs: Rotation3DFloat) -> Rotation3DFloat
```

#### Discussion

For example, multiplying an angle of 90° by `0.5`, returns an angle of 45°:

```None
 let rotation = Rotation3DFloat(angle: Angle2DFloat(degrees: 90),
                           axis: .init(x: 0, y: 1, z: 0))
 let rotated = ( 0.5 * rotation).angle.degrees
 print(rotated) // prints "45.0"
```

- Note This function returns the longest path where the angle is greater than 180°,

## Parameters

- `lhs`: The interpolation parameter
- `rhs`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/*(_:_:)-99umr)*