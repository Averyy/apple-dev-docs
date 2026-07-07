# GaussianSplatResource.ActivationFunction.sigmoid

**Framework**: RealityKit  
**Kind**: case

Applies a sigmoid function to each value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case sigmoid
```

#### Discussion

Choose this when your values are unbounded logits that map to the 0 to 1 range, as opacity often is. The framework computes *f(x) = 1 / (1 + e^(-x))*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction/sigmoid)*