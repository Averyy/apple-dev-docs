# init(name:jointWeights:)

**Framework**: RealityKit  
**Kind**: init

Creates a blend mask with the specified parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(name: String, jointWeights: [String : Float])
```

## Parameters

- `name`: The unique name of the blend mask within the skeleton
- `jointWeights`: Dictionary of joint weights keyed by joint name (0-1 range). Joints not in dictionary default to 1.0 (full animation effect).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/blendmask/init(name:jointweights:))*