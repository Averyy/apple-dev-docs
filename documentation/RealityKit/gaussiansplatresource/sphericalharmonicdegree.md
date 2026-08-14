# GaussianSplatResource.SphericalHarmonicDegree

**Framework**: RealityKit  
**Kind**: enum

The amount of view-dependent color detail stored per splat.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SphericalHarmonicDegree
```

#### Overview

Higher degrees capture higher-frequency color variation as the viewing angle changes, at the cost of more data per splat.

## Topics

### Enumeration Cases
- [GaussianSplatResource.SphericalHarmonicDegree.first](gaussiansplatresource/sphericalharmonicdegree/first.md)
  12 values: three first-order lobes plus the degree-zero diffuse color.
- [GaussianSplatResource.SphericalHarmonicDegree.second](gaussiansplatresource/sphericalharmonicdegree/second.md)
  27 values: five second-order lobes plus the degree-one coefficients.
- [GaussianSplatResource.SphericalHarmonicDegree.third](gaussiansplatresource/sphericalharmonicdegree/third.md)
  48 values: seven third-order lobes plus the degree-two coefficients.
- [GaussianSplatResource.SphericalHarmonicDegree.zero](gaussiansplatresource/sphericalharmonicdegree/zero.md)
  3 values: diffuse color only.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/sphericalharmonicdegree)*