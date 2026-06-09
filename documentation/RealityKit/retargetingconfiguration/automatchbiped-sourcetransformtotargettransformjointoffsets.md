# automatchBiped(_:sourceTransform:to:targetTransform:jointOffsets:)

**Framework**: RealityKit  
**Kind**: method

Creates a retargeting configuration for bipedal characters with custom root transforms.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func automatchBiped(_ sourceSkeleton: SkeletonResource, sourceTransform: Transform = .identity, to targetSkeleton: SkeletonResource, targetTransform: Transform = .identity, jointOffsets: [String : simd_quatf] = [:]) throws -> RetargetingConfiguration
```

#### Return Value

A configured retargeting instance ready for animation processing.

#### Discussion

This overload allows you to specify custom transforms for the root bones of both skeletons, which is useful when the characters are positioned or oriented differently in their bind poses. The function applies the transforms during the automatic matching process to establish proper correspondences.

The automatic matching algorithm has the same joint requirements and behavior as [`automatchBiped(_:to:jointOffsets:)`](retargetingconfiguration/automatchbiped(_:to:jointoffsets:).md).

#### Example

```swift
do {
    // Source character facing +Z, target facing +X
    let sourceTransform = Transform(rotation: simd_quatf(angle: 0, axis: simd_float3(0, 1, 0)))
    let targetTransform = Transform(rotation: simd_quatf(angle: .pi/2, axis: simd_float3(0, 1, 0)))

    let config = try RetargetingConfiguration.automatchBiped(
        sourceSkeleton,
        sourceTransform: sourceTransform,
        to: targetSkeleton,
        targetTransform: targetTransform
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
- `sourceTransform`: Transform applied to the source skeleton’s root during matching (defaults to identity).
- `targetSkeleton`: The skeleton that will receive the re-targeted animation.
- `targetTransform`: Transform applied to the target skeleton’s root during matching (defaults to identity).
- `jointOffsets`: Optional quaternion offsets applied to specific joints during configuration creation. Keys must match joint names in the target skeleton. The function applies offsets on top of the automatically detected joint correspondences and bakes them into the configuration.

## See Also

- [static func automatchBiped(SkeletonResource, to: SkeletonResource, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchbiped(_:to:jointoffsets:).md)
  Creates a retargeting configuration for bipedal characters using automatic joint matching.
- [static func automatchQuadruped(SkeletonResource, sourceTransform: Transform, to: SkeletonResource, targetTransform: Transform, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchquadruped(_:sourcetransform:to:targettransform:jointoffsets:).md)
  Creates a retargeting configuration for quadrupedal characters using automatic joint matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/retargetingconfiguration/automatchbiped(_:sourcetransform:to:targettransform:jointoffsets:))*