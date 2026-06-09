# id

**Framework**: RealityKit  
**Kind**: property

The identifier of the blend mask, derived from its name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var id: String { get }
```

## See Also

- [var jointWeights: [String : Float]](skeletonresource/blendmask/jointweights.md)
  Dictionary of joint weights keyed by joint name. Each weight corresponds to a joint in the skeleton, controlling how much that joint is affected by animations using this mask. Values range from 0.0 (no effect) to 1.0 (full effect). Joints not present in the dictionary are treated as having weight 1.0 (full animation effect).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/blendmask/id)*