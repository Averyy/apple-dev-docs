# init(named:skeletalJointName:offsetPosition:offsetOrientation:)

**Framework**: RealityKit  
**Kind**: init

Creates a geometric pin that attaches to a skeletal joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(named name: String, skeletalJointName: String, offsetPosition: SIMD3<Float> = SIMD3<Float>(0, 0, 0), offsetOrientation: simd_quatf = simd_quatf(ix: 0, iy: 0, iz: 0, r: 1))
```

#### Discussion

The current animated joint transform defines the position and orientation of the pin.

## Parameters

- `name`: Name of the   in the namespace of the owning entity.
- `skeletalJointName`: Name of the skeletal joint that this pin attaches to.
- `offsetPosition`: Adjustment of the   position in the coordinate frame of the joint.
- `offsetOrientation`: Adjustment of the   orientation in the coordinate frame of the joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/geometricpin/init(named:skeletaljointname:offsetposition:offsetorientation:))*