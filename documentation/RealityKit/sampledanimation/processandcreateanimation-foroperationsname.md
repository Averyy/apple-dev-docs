# processAndCreateAnimation(for:operations:name:)

**Framework**: RealityKit  
**Kind**: method

Processes skeletal animation with the specified operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func processAndCreateAnimation(for skeleton: SkeletonResource? = nil, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String = "") throws -> any AnimationDefinition
```

#### Return Value

An `AnimationDefinition` containing the processed animation. If root motion extraction is performed, returns an `AnimationGroup` containing both the skeletal animation (`SampledAnimation<JointTransforms>`) and extracted root motion (`SampledAnimation<Transform>`). Otherwise returns a `SampledAnimation<JointTransforms>`.

#### Discussion

Applies a series of skeletal animation processing operations to create a new animation. The function executes operations in the order specified. If skeleton is nil, only additive operations are supported.

> **Note**: An error if validation fails. All errors provide descriptive messages via their `localizedDescription` property. Common validation failures include: - Duplicate operation types in a single call (e.g., two `extractRootMotion` operations).
- Both `extractRootMotion` and `removeAnimation(for:)` operations in the same call.
- Operations requiring a skeleton when skeleton parameter is nil.
- Joint name does not exist in the skeleton for root motion extraction or removal.
- Base animation has a different sample rate than the source animation for `convertToAdditive`.

## Parameters

- `skeleton`: The skeleton resource for the animation; required for all operations except [`convertToAdditive(baseAnimation:)`](sampledanimation/skeletalanimationoperation/converttoadditive(baseanimation:).md) and [`convertToAdditiveUsingFirstSample()`](sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample().md).
- `operations`: Operations to perform on the animation. Must not be empty.
- `name`: Name for the processed animation.

## See Also

- [func processAndCreateAnimation(retargeting: RetargetingConfiguration, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String) throws -> any AnimationDefinition](sampledanimation/processandcreateanimation(retargeting:operations:name:).md)
  Processes skeletal animation with the specified retargeting and operations.
- [SampledAnimation.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation.md)
  Operations that can be performed on skeletal animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/processandcreateanimation(for:operations:name:))*