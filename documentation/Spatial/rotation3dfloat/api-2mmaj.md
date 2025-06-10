# *(_:_:)

**Framework**: Spatial  
**Kind**: op

Calculates the spherical linear interpolation between the identity rotation and the LHS rotation at the RHS interpolation parameter.

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
static func * (lhs: Rotation3DFloat, rhs: Float) -> Rotation3DFloat
```

#### Discussion

For example, multiplying an angle of 90° by `0.5`, returns an angle of 45°:

```None
 let rotation = Rotation3DFloat(angle: Angle2DFloat(degrees: 90),
                           axis: .init(x: 0, y: 1, z: 0))
 let rotated = (rotation * 0.5).angle.degrees
 print(rotated) // prints "45.0"
```

- Note This function returns the longest path where the angle is greater than 180°,

## Parameters

- `lhs`: The rotation
- `rhs`: The interpolation parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/*(_:_:)-2mmaj)*