# jointWeights

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Dictionary of joint weights keyed by joint name. Each weight corresponds to a joint in the skeleton, controlling how much that joint is affected by animations using this mask. Values range from 0.0 (no effect) to 1.0 (full effect). Joints not present in the dictionary are treated as having weight 1.0 (full animation effect).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var jointWeights: [String : Float]
```

## See Also

### Accessing mask values
- [var id: String](./id.md)
  The identifier of the blend mask, derived from its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/blendmask/jointweights)*