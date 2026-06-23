# GaussianSplatResource.SphericalHarmonicDegree

**Framework**: RealityKit  
**Kind**: enum

Spherical harmonic (SH) coefficients encode view-dependent color information. Higher degrees produce higher frequency variance at the cost of additional data per splat:

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SphericalHarmonicDegree
```

#### Overview

- **Zero** — 3 values (diffuse color only)
- **First** — 12 total values (3 new lobes + level zero diffuse)
- **Second** — 27 total values (5 new lobes + level one SHs)
- **Third** — 48 total values (7 new lobes + level two SHs)

## Topics

### Enumeration Cases
- [GaussianSplatResource.SphericalHarmonicDegree.first](gaussiansplatresource/sphericalharmonicdegree/first.md)
- [GaussianSplatResource.SphericalHarmonicDegree.second](gaussiansplatresource/sphericalharmonicdegree/second.md)
- [GaussianSplatResource.SphericalHarmonicDegree.third](gaussiansplatresource/sphericalharmonicdegree/third.md)
- [GaussianSplatResource.SphericalHarmonicDegree.zero](gaussiansplatresource/sphericalharmonicdegree/zero.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/sphericalharmonicdegree)*