# GaussianSplatResource.ActivationFunction

**Framework**: RealityKit  
**Kind**: enum

Raw scale and opacity values from a trained Gaussian splat model often need a mathematical transformation before rendering. The [`GaussianSplatResource.ActivationFunction`](gaussiansplatresource/activationfunction.md) enumeration defines these transformations:

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ActivationFunction
```

#### Overview

- [`GaussianSplatResource.ActivationFunction.identity`](gaussiansplatresource/activationfunction/identity.md) — Uses the values as-is. Choose this when your data is already transformed. This is the default.
- [`GaussianSplatResource.ActivationFunction.exponential`](gaussiansplatresource/activationfunction/exponential.md) — Applies *f(x) = e^x* to incoming values.
- [`GaussianSplatResource.ActivationFunction.sigmoid`](gaussiansplatresource/activationfunction/sigmoid.md) — Applies *f(x) = 1 / (1 + e^(-x))* to incoming values.

## Topics

### Enumeration Cases
- [GaussianSplatResource.ActivationFunction.exponential](gaussiansplatresource/activationfunction/exponential.md)
- [GaussianSplatResource.ActivationFunction.identity](gaussiansplatresource/activationfunction/identity.md)
- [GaussianSplatResource.ActivationFunction.sigmoid](gaussiansplatresource/activationfunction/sigmoid.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction)*