# PortalComponent.ClippingPlane

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A representation of a portal as an infinite plane.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ClippingPlane
```

## Overview

Use this type with [`init(target:clippingPlane:)`](./init%28target,clippingplane%29.md) to initialize a portal component with the clipping feature in an enabled state.

## Topics

### Initializers
- [init(position: SIMD3<Float>, normal: SIMD3<Float>)](./clippingplane-swift.struct/init%28position,normal%29.md)
  Creates a clipping plane at a position and normal direction.
### Instance Properties
- [var normal: SIMD3<Float>](./clippingplane-swift.struct/normal.md)
  The normal of the clipping plane.
- [var position: SIMD3<Float>](./clippingplane-swift.struct/position.md)
  The position of the clipping plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingplane-swift.struct)*