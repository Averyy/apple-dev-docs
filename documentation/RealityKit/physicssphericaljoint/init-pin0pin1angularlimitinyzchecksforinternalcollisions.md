# init(pin0:pin1:angularLimitInYZ:checksForInternalCollisions:)

**Framework**: RealityKit  
**Kind**: init

Creates a new spherical joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(pin0: GeometricPin, pin1: GeometricPin, angularLimitInYZ: (Float, Float)? = nil, checksForInternalCollisions: Bool = false)
```

#### Discussion

An elliptical cone is formed around the x-axis to limit the motion of `pin1` if `angularLimitInYZ` is defined.

If `angularLimitInYZ` is undefined, `pin1` has full 360º rotational freedom in all axes.

## Parameters

- `pin0`: The local position and orientation on the first entity.
- `pin1`: The local position and orientation on the second entity.
- `angularLimitInYZ`: A maximum value of rotation in radians from the y and z axes if defined.
- `checksForInternalCollisions`: A Boolean that indicates whether the joint   checks for collisions between the two   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssphericaljoint/init(pin0:pin1:angularlimitinyz:checksforinternalcollisions:))*