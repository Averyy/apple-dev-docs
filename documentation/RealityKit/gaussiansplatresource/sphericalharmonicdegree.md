# GaussianSplatResource.SphericalHarmonicDegree

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The amount of view-dependent color detail stored per splat.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SphericalHarmonicDegree
```

## Overview

Higher degrees capture higher-frequency color variation as the viewing angle changes, at the cost of more data per splat.

## Topics

### Enumeration Cases
- [GaussianSplatResource.SphericalHarmonicDegree.first](./sphericalharmonicdegree/first.md)
  12 values: three first-order lobes plus the degree-zero diffuse color.
- [GaussianSplatResource.SphericalHarmonicDegree.second](./sphericalharmonicdegree/second.md)
  27 values: five second-order lobes plus the degree-one coefficients.
- [GaussianSplatResource.SphericalHarmonicDegree.third](./sphericalharmonicdegree/third.md)
  48 values: seven third-order lobes plus the degree-two coefficients.
- [GaussianSplatResource.SphericalHarmonicDegree.zero](./sphericalharmonicdegree/zero.md)
  3 values: diffuse color only.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/sphericalharmonicdegree)*