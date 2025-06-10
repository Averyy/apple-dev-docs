# set(named:skeletalJointName:position:orientation:)

**Framework**: RealityKit  
**Kind**: method

Creates and adds a geometric pin to the entity’s skeletal joint, and returns the geometric pin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor func set(named name: String, skeletalJointName: String, position: SIMD3<Float> = SIMD3<Float>(0, 0, 0), orientation: simd_quatf = simd_quatf(ix: 0, iy: 0, iz: 0, r: 1)) -> GeometricPin
```

#### Return Value

A `GeometricPin`, identifying the newly added reference frame on the [`Entity`](entity.md).

#### Discussion

The pin is added to the entity’s [`GeometricPinsComponent`](geometricpinscomponent.md).

## Parameters

- `name`: Name of the   in the namespace of the owning entity.
- `skeletalJointName`: The name of the skeletal joint in the namespace of the owning entity.
- `position`: The position of the pin, in local space of the joint.
- `orientation`: The orientation of the pin, in local space of the joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygeometricpins/set(named:skeletaljointname:position:orientation:))*