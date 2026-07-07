# GaussianSplatResource.ActivationFunction

**Framework**: RealityKit  
**Kind**: enum

A transformation the framework applies to raw scale or opacity values before rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ActivationFunction
```

#### Overview

Trained Gaussian splat models often store scale and opacity in a form that needs a mathematical transformation. Choose the function that matches how your data was trained.

## Topics

### Enumeration Cases
- [GaussianSplatResource.ActivationFunction.exponential](gaussiansplatresource/activationfunction/exponential.md)
  Applies an exponential function to each value.
- [GaussianSplatResource.ActivationFunction.identity](gaussiansplatresource/activationfunction/identity.md)
  Uses the values without transformation.
- [GaussianSplatResource.ActivationFunction.sigmoid](gaussiansplatresource/activationfunction/sigmoid.md)
  Applies a sigmoid function to each value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction)*