# extractRootMotion(jointName:options:lockPosition:)

**Framework**: RealityKit  
**Kind**: method

Extracts root motion from the specified joint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions = .translationXZ, lockPosition: Transform? = nil) -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](sampledanimation/skeletalanimationoperation.md) that, when processed, produces an [`AnimationGroup`](animationgroup.md) containing both the modified skeletal animation and the extracted transform sampled animation used for root motion.

#### Discussion

Removes the specified transform components from the joint and returns them as a separate `SampledAnimation<Transform>` in the resulting [`AnimationGroup`](animationgroup.md). The skeletal animation will have the extracted motion removed. The returned `SampledAnimation<Transform>` has [`bindTarget`](sampledanimation/bindtarget.md) set to [`BindTarget.rootMotion`](bindtarget/rootmotion.md) automatically — playing the group drives the entity’s root motion and emits [`AnimationEvents.RootMotionDidUpdate`](animationevents/rootmotiondidupdate.md) events.

When you extract root motion, the function returns an [`AnimationGroup`](animationgroup.md) containing both the skeletal animation and the root motion animation. Playing back this group triggers root motion events in sync with the skeletal animation. The event callback receives the delta transform moved between the last frame and the current frame. If no event handler subscribes to the root motion on the target entity, the system automatically applies the delta to the entity’s transform.

## Parameters

- `jointName`: Name of the joint to extract root motion from.
- `options`: Transform components to extract.
- `lockPosition`: Position to lock the root joint to after extraction.

## See Also

- [SampledAnimation.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions.md)
  Options for controlling root motion extraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/extractrootmotion(jointname:options:lockposition:))*