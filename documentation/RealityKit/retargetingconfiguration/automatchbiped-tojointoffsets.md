# automatchBiped(_:to:jointOffsets:)

**Framework**: RealityKit  
**Kind**: method

Creates a retargeting configuration for bipedal characters using automatic joint matching.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func automatchBiped(_ sourceSkeleton: SkeletonResource, to targetSkeleton: SkeletonResource, jointOffsets: [String : simd_quatf] = [:]) throws -> RetargetingConfiguration
```

#### Return Value

A configured retargeting instance ready for animation processing.

#### Discussion

This method uses an automatic matching algorithm to analyze both skeletal hierarchies and establish correspondences between key joints. The algorithm performs joint identification to locate required anatomical landmarks and generates a retargeting configuration accordingly.

##### Required Joints

The algorithm identifies and requires the following joints in both skeletons:

- **Core**: Hips, Spine Base, Chest, Neck Base, Head
- **Arms**: Left/Right Shoulder, Upper Arm, Elbow, Wrist
- **Legs**: Left/Right Upper Leg, Knee, Ankle, Toe

##### Optional Joints

The algorithm can optionally identify and use:

- Toe End joints (Left/Right Toe End)
- Finger Base joints (Left/Right Finger Base 0-4)

##### Algorithm Behavior

- Performs automatic joint identification using joint names and hierarchical structure.
- Supports T-pose and A-pose configurations.
- May optimize the resulting configuration by culling unnecessary joints.
- Applies joint offsets on top of automatically detected correspondences during configuration creation.

#### Example

```swift
do {
    // Basic biped retargeting
    let config = try RetargetingConfiguration.automatchBiped(
        humanoidSourceSkeleton,
        to: humanoidTargetSkeleton
    )

    // With joint adjustments
    let jointOffsets: [String: simd_quatf] = [
        "LeftShoulder": simd_quatf(angle: .pi / 18, axis: simd_float3(0, 0, 1)),
        "RightWrist": simd_quatf(angle: -.pi / 36, axis: simd_float3(1, 0, 0))
    ]
    let refinedConfig = try RetargetingConfiguration.automatchBiped(
        humanoidSourceSkeleton,
        to: humanoidTargetSkeleton,
        jointOffsets: jointOffsets
    )
} catch {
    print("Failed to create retargeting configuration: \(error.localizedDescription)")
}
```

> **Note**: An error if configuration creation fails. All errors provide descriptive messages via their `localizedDescription` property. Common failures include: - A joint offset was specified for a joint name that doesn’t exist in the target skeleton.
- The algorithm could not identify required joints in one or both skeletons.
- Joint identification or rig generation failed.

## Parameters

- `sourceSkeleton`: The skeleton of the animation to retarget.
- `targetSkeleton`: The skeleton that will receive the re-targeted animation.
- `jointOffsets`: Optional quaternion offsets applied to specific joints during configuration creation. Keys must match joint names in the target skeleton. The function applies offsets on top of the automatically detected joint correspondences and bakes them into the configuration.

## See Also

- [static func automatchBiped(SkeletonResource, sourceTransform: Transform, to: SkeletonResource, targetTransform: Transform, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchbiped(_:sourcetransform:to:targettransform:jointoffsets:).md)
  Creates a retargeting configuration for bipedal characters with custom root transforms.
- [static func automatchQuadruped(SkeletonResource, sourceTransform: Transform, to: SkeletonResource, targetTransform: Transform, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchquadruped(_:sourcetransform:to:targettransform:jointoffsets:).md)
  Creates a retargeting configuration for quadrupedal characters using automatic joint matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/retargetingconfiguration/automatchbiped(_:to:jointoffsets:))*