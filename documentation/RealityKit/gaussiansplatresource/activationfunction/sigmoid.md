# GaussianSplatResource.ActivationFunction.sigmoid

**Framework**: RealityKit  
**Kind**: case

Applies a sigmoid function to each value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case sigmoid
```

#### Discussion

Choose this when your values are unbounded logits that map to the 0 to 1 range, as opacity often is. The framework computes *f(x) = 1 / (1 + e^(-x))*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction/sigmoid)*