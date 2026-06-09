# RetargetingConfiguration

**Framework**: RealityKit  
**Kind**: class

A configuration for retargeting skeletal animations between different skeletons.

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
class RetargetingConfiguration
```

#### Overview

`RetargetingConfiguration` enables the transfer of animations from one skeleton to another, automatically mapping joints and adapting poses to accommodate different skeletal structures. This is particularly useful for applying animations across different character models or creatures.

#### Usage

Create configurations using the static factory methods for common skeleton types:

- [`automatchBiped(_:to:jointOffsets:)`](retargetingconfiguration/automatchbiped(_:to:jointoffsets:).md) for humanoid/bipedal characters
- [`automatchQuadruped(_:sourceTransform:to:targetTransform:jointOffsets:)`](retargetingconfiguration/automatchquadruped(_:sourcetransform:to:targettransform:jointoffsets:).md) for four-legged creatures

#### Example

```swift
do {
    // Basic biped retargeting
    let config = try RetargetingConfiguration.automatchBiped(
        sourceCharacterSkeleton,
        to: targetCharacterSkeleton
    )

    // With joint offset adjustments applied during configuration creation
    let jointOffsets: [String: simd_quatf] = [
        "LeftShoulder": simd_quatf(angle: 0.1, axis: simd_float3(0, 1, 0)),
        "RightShoulder": simd_quatf(angle: -0.1, axis: simd_float3(0, 1, 0))
    ]
    let configWithOffsets = try RetargetingConfiguration.automatchBiped(
        sourceCharacterSkeleton,
        to: targetCharacterSkeleton,
        jointOffsets: jointOffsets
    )
} catch {
    print("Failed to create retargeting configuration: \(error.localizedDescription)")
}
```

#### Performance Considerations

- Configuration creation is computationally expensive and should be cached when possible.
- The automatic matching algorithm analyzes skeleton hierarchies to establish joint correspondences.
- Joint offsets are baked into the configuration during creation, not applied at runtime.

## Topics

### Creating a configuration
- [static func automatchBiped(SkeletonResource, sourceTransform: Transform, to: SkeletonResource, targetTransform: Transform, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchbiped(_:sourcetransform:to:targettransform:jointoffsets:).md)
  Creates a retargeting configuration for bipedal characters with custom root transforms.
- [static func automatchBiped(SkeletonResource, to: SkeletonResource, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchbiped(_:to:jointoffsets:).md)
  Creates a retargeting configuration for bipedal characters using automatic joint matching.
- [static func automatchQuadruped(SkeletonResource, sourceTransform: Transform, to: SkeletonResource, targetTransform: Transform, jointOffsets: [String : simd_quatf]) throws -> RetargetingConfiguration](retargetingconfiguration/automatchquadruped(_:sourcetransform:to:targettransform:jointoffsets:).md)
  Creates a retargeting configuration for quadrupedal characters using automatic joint matching.
### Accessing the skeletons
- [var sourceSkeleton: SkeletonResource](retargetingconfiguration/sourceskeleton.md)
  The skeleton the source animation targets.
- [var targetSkeleton: SkeletonResource](retargetingconfiguration/targetskeleton.md)
  The skeleton the retargeting animates.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SkeletonResource](skeletonresource.md)
  Represents a skeleton asset with joint hierarchy and animation capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/retargetingconfiguration)*