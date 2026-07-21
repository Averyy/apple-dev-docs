# animationEvaluation

**Framework**: RealityKit  
**Kind**: property

Animation-evaluation data baked into this resource at construction time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final let animationEvaluation: SkeletonResource.AnimationEvaluation
```

#### Discussion

Fixed at construction and immutable for the lifetime of the resource — every reader observes the same value the initializer received.

## See Also

- [SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.struct.md)
  A bundle of additional animation-related skeletal data the runtime consumes when evaluating animations against this skeleton.
- [SkeletonResource.BlendMask](skeletonresource/blendmask.md)
  Describes a single blend mask for selective animation control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/animationevaluation-swift.property)*