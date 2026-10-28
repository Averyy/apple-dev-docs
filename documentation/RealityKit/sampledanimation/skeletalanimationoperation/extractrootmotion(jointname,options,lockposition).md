# extractRootMotion(jointName:options:lockPosition:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Extracts root motion from the specified joint.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions = .translationXZ, lockPosition: Transform? = nil) -> SampledAnimation<Value>.SkeletalAnimationOperation
```

## Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](../skeletalanimationoperation.md) that, when processed, produces an [`AnimationGroup`](../../animationgroup.md) containing both the modified skeletal animation and the extracted transform sampled animation used for root motion.

## Discussion

Removes the specified transform components from the joint and returns them as a separate `SampledAnimation<Transform>` in the resulting [`AnimationGroup`](../../animationgroup.md). The skeletal animation will have the extracted motion removed. The returned `SampledAnimation<Transform>` has [`bindTarget`](../bindtarget.md) set to [`BindTarget.rootMotion`](../../bindtarget/rootmotion.md) automatically — playing the group drives the entity’s root motion and emits [`AnimationEvents.RootMotionDidUpdate`](../../animationevents/rootmotiondidupdate.md) events.

When you extract root motion, the function returns an [`AnimationGroup`](../../animationgroup.md) containing both the skeletal animation and the root motion animation. Playing back this group triggers root motion events in sync with the skeletal animation. The event callback receives the delta transform moved between the last frame and the current frame. If no event handler subscribes to the root motion on the target entity, the system automatically applies the delta to the entity’s transform.

## Parameters

- `jointName`: Name of the joint to extract root motion from.
- `options`: Transform components to extract.
- `lockPosition`: Position to lock the root joint to after extraction.

## See Also

### Extracting root motion
- [SampledAnimation.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions.md)
  Options for controlling root motion extraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/extractrootmotion(jointname:options:lockposition:))*